# Axial-symmetric indenter model
# MP, 2021-11; adapted for Abaqus/Python course 2022-10

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os, shutil
import numpy as np

DIR0 = os.path.abspath('')
TOL = 1e-4
session.journalOptions.setValues(replayGeometry=COORDINATE,
        		                 recoverGeometry=COORDINATE)

def make_dir(dir_name, if_change=0, if_clear=0):
    # creates and changes into a subdirectory
    if os.path.exists(dir_name) == 0:
        os.mkdir(dir_name)
    else:
        if if_clear:
            shutil.rmtree(dir_name)
            os.mkdir(dir_name)
    #dir1 = dir_abs + "//" + dir_name
    if if_change:
        os.chdir(dir_name)
    return dir_name

# Funktionen vom Modell
# ------------------------------------------------------------------
def make_geom(model,r_tip,ang_tip,(b,h,b0,h0),(size_fine,size_coarse),mu,if_plastic=1):
    # Indenter Part
    # --------------------------
    s = model.ConstrainedSketch(name='indenter', sheetSize=200.0)

    ang_mid = (90.-ang_tip)*pi/180.
    out_point = (r_tip*sin(ang_mid),r_tip*(1-cos(ang_mid)))

    s.ArcByCenterEnds(center=(0,r_tip), point1=(0,0), point2=out_point, 
                    direction=COUNTERCLOCKWISE)

    dy0 = r_tip*(1-cos(ang_tip*pi/180.))/cos(ang_tip*pi/180.)
    s.Line(point1=out_point, point2=(b/2., b/(2*tan(ang_tip*pi/180.))-dy0))
    # s.Line(point1=out_point, point2=(b/2., b/(2*tan(ang_tip*pi/180.))+dy0))

    s.ConstructionLine(point1=(0,0), point2=(0,1))

    p = model.Part(name='Indenter', dimensionality=AXISYMMETRIC, 
                type=DISCRETE_RIGID_SURFACE)
    p.BaseWire(sketch=s)

    rp = p.ReferencePoint(point=(0,r_tip,0))

    # Sets and Surfaces
    p.Set(name='rp',referencePoints=(p.referencePoints[rp.id],))
    p.Surface(side2Edges=p.edges, name='contact')

    p.seedPart(size=size_fine)
    p.generateMesh()

    # Specimen Part
    # --------------------------

    s2 = model.ConstrainedSketch(name='specimen', sheetSize=200.0)
    s2.ConstructionLine(point1=(0,0), point2=(0,1))
    s2.rectangle(point1=(0,-h), point2=(b,0))

    p2 = model.Part(dimensionality=AXISYMMETRIC, name='Specimen',
                    type=DEFORMABLE_BODY)
    p2.BaseShell(sketch=s2)

    # partition
    s2_p = model.ConstrainedSketch(name='partition', sheetSize=200.0)
    s2_p.rectangle(point1=(0,-h0), point2=(b0,0))

    p2.PartitionFaceBySketch(faces=p2.faces, sketch=s2_p)

    p2.seedPart(size=size_coarse)
    p2.seedEdgeBySize(edges=p2.edges.getByBoundingBox(yMin=-h0-TOL,xMax=b0+TOL),
                    size=size_fine, constraint=FINER)
    p2.generateMesh()

    # Sets and Surfaces
    p2.Set(name='all',faces=p2.faces)
    p2.Set(name='xsym',edges=p2.edges.getByBoundingBox(xMax=TOL))
    p2.Set(name='ysym',edges=p2.edges.getByBoundingBox(yMax=-h+TOL))
    p2.Surface(name='contact',side1Edges=p2.edges.getByBoundingBox(xMax=b0+TOL,yMin=-TOL))

    # Instances, Sections
    # --------------------------

    ass = model.rootAssembly
    inst = ass.Instance(name='Indenter', part=p, dependent=ON)
    inst2 = ass.Instance(name='Specimen', part=p2, dependent=ON)

    # Bild ausgeben vom Modell
    vp = session.viewports['Viewport: 1']
    vp.setValues(displayedObject=ass)

    vp.assemblyDisplay.setValues(mesh=ON)
    vp.assemblyDisplay.meshOptions.setValues(meshTechnique=ON)
    vp.view.fitView()
    session.printOptions.setValues(vpDecorations=OFF, reduceColors=False)
    session.printToFile(fileName='mesh-indent', format=PNG, canvasObjects=(vp, ))

    # unser Material erzeugen
    mat = model.Material(name='PET')
    mat.Elastic(table=((3000,0.35), ))
    if if_plastic:
        mat.Plastic(table=((30., 0.0), (30.+600., 1.0)))
    else:
        mat.Viscoelastic(domain=TIME, time=PRONY, table=((0.4, 0.0, 1000.0), ))

    # Section erstellen und zuweisen
    model.HomogeneousSolidSection(material='PET', name='PET', thickness=None)
    p2.SectionAssignment(region=p2.sets['all'], sectionName='PET',
                        thicknessAssignment=FROM_SECTION)

    # Interaction, BCs, Load
    # --------------------------

    ip = model.ContactProperty('int-prop')

    if mu == 0:
        ip.TangentialBehavior(formulation=FRICTIONLESS)
    else:
        ip.TangentialBehavior(formulation=PENALTY, table=((mu,),), shearStressLimit=None,
                            maximumElasticSlip=FRACTION, fraction=0.005)

    ip.NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON, contactStiffness=DEFAULT, 
                    contactStiffnessScaleFactor=1.0, clearanceAtZeroContactPressure=0.0, 
                    constraintEnforcementMethod=AUGMENTED_LAGRANGE)
    try:
        model.SurfaceToSurfaceContactStd(name='contact', createStepName='Initial', sliding=FINITE,
                                        master=inst.surfaces['contact'], slave=inst2.surfaces['contact'], 
                                        interactionProperty='int-prop')
    except: # bei Version 2022: main und secondary
        model.SurfaceToSurfaceContactStd(name='contact', createStepName='Initial', sliding=FINITE,
                                        main=inst.surfaces['contact'], secondary=inst2.surfaces['contact'], 
                                        interactionProperty='int-prop')
    return inst, inst2

def make_loads(model,inst,inst2,uy,fy,max_inc,job_name,if_plastic,if_force=0):
    #
    model.DisplacementBC(name='xsym', createStepName='Initial', region=inst2.sets['xsym'],
                        u1=0)
    model.DisplacementBC(name='ysym', createStepName='Initial', region=inst2.sets['ysym'],
                        u2=0)
    
    model.StaticStep(name='load-u', previous='Initial', maxNumInc=1000, initialInc=max_inc, 
                     minInc=1e-08, maxInc=max_inc, nlgeom=ON)

    model.HistoryOutputRequest(name='H-Output-RP', createStepName='load-u', variables=('U2','RF2','CF2'),
                               region=inst.sets['rp'])
    
    # Step und Loads
    if not if_force:        
        bc_u2 = model.DisplacementBC(name='uy', createStepName='load-u', region=inst.sets['rp'],
                                u1=0, ur3=0, u2=-uy)
        step_name = 'load-u'
    else:
        bc_u2 = model.DisplacementBC(name='uy', createStepName='load-u', region=inst.sets['rp'],
                                u1=0, ur3=0, u2=-0.0001)
        # Kraft aufbringen
        model.StaticStep(name='load-f', previous='load-u', maxNumInc=1000, initialInc=max_inc, 
                            minInc=1e-08, maxInc=max_inc, nlgeom=ON)
        bc_u2.setValuesInStep(stepName='load-f', u2=FREED)
        # Kraft
        model.ConcentratedForce(name='load-f', createStepName='load-f', region=inst.sets['rp'],
                                cf2=-fy)
        step_name = 'load-f'
    
    # Entlasten bzw. halten
    if if_plastic:
        model.StaticStep(name='unload', previous=step_name, maxNumInc=1000, initialInc=max_inc, 
                        minInc=1e-08, maxInc=max_inc, nlgeom=ON)
        bc_u2.setValuesInStep(stepName='unload', u2=0.0)
    else:
        # sonst Viskoelastisch
        # extra step: visco, Relaxieren
        model.ViscoStep(name='hold', previous=step_name, 
                        description='Relaxieren in 10 h', timePeriod=36000.0, 
                        initialInc=3600.0, minInc=0.36, maxInc=3600.0, cetol=0.01)

    # Rechnen und auswerten
    # --------------------------
    # Modell speicher, Job erstellen und rechnen
    mdb.saveAs(job_name)
    job = mdb.Job(name=job_name, model='Model-1', type=ANALYSIS)

    job.submit()
    job.waitForCompletion()
    return

def eval_fu_curve(odb_name):
    # open the odb with the odb_name
    odb = session.openOdb(name=odb_name+'.odb')

    u_list = []
    rf_list = []

    for i_step,step in enumerate(odb.steps.values()):
        hr = step.historyRegions.values()[1]
        rf_temp = np.array(hr.historyOutputs['RF2'].data)[:,1]
        u_temp = np.array(hr.historyOutputs['U2'].data)[:,1]
        if i_step == 0:
            rf_list += list(rf_temp)
            u_list += list(u_temp)
        else:
            rf_list += list(rf_temp[1:])
            u_list += list(u_temp[1:])

    print(u_list,rf_list)
    np.savetxt(odb_name+'-res.dat', np.column_stack((u_list,rf_list)), header='U2 (mm), RF2 (N)',
               delimiter=', ')
    return

def make_hardness_model(dir_name,r_tip,ang_tip,(b,h,b0,h0),(size_fine,size_coarse),
                        mu,uy,fy,max_inc,if_plastic=1,if_force=0):
    # complete model creation in one function
    if if_plastic:
        job_name = 'indenter-pl'
    else:
        job_name = 'indenter-visco'
    #
    Mdb()
    model = mdb.models['Model-1']
    #
    make_dir(dir_name,if_change=1)
    #
    inst, inst2 = make_geom(model,r_tip,ang_tip,(b,h,b0,h0),(size_fine,size_coarse),
                            mu,if_plastic)
    #
    make_loads(model,inst,inst2,uy,fy,max_inc,job_name,if_plastic,if_force)
    #
    eval_fu_curve(job_name)
    os.chdir(DIR0)
    return

# Parameter vom Modell (N-mm-s)
# ------------------------------------------------------
r_tip = 0.1
ang_tip = 45.

b,h,b0,h0 = 1,0.5, 0.3, 0.15

mu = 0.3
uy,max_inc = 0.1, 0.1
fy = 3000.

size_fine, size_coarse = 0.007, 0.05

dir_name = 'indenter-v2'
# ----------------------------------------------------------

# run the model
make_hardness_model(dir_name,r_tip,ang_tip,(b,h,b0,h0),(size_fine,size_coarse),
                        mu,uy,fy,max_inc,if_plastic=1,if_force=0)
