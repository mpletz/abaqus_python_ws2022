# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by p1340760 on Thu Oct 20 14:08:49 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=101.068748474121, 
    height=129.855545043945)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile(
    'C:/Users/p1340760/Desktop/Python-Projekte/_Lehre/abaqus_python_ws2022/unit-3/model-03-part.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['draw-spline-sketch'].ConstrainedSketch(name='__edit__', 
    objectToCopy=mdb.models['draw-spline-sketch'].sketches['waves'])
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.unsetPrimaryObject()
del mdb.models['draw-spline-sketch'].sketches['__edit__']
s1 = mdb.models['draw-spline-sketch'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.sketchOptions.setValues(gridOrigin=(12.5, 3.99998426437378))
#: Warning: Grid center was moved to the sketch center.
s1.retrieveSketch(sketch=mdb.models['draw-spline-sketch'].sketches['waves'])
session.viewports['Viewport: 1'].view.fitView()
#: Info: 4 entities copied from waves.
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.9069, 
    farPlane=57.0883, width=31.6043, height=15.0964, cameraPosition=(13.0579, 
    3.69887, 52.4976), cameraTarget=(13.0579, 3.69887, 0))
s1.move(vector=(12.5, 3.99998426437378), objectList=(g.findAt((0.0, 3.0)), 
    g.findAt((25.0, 3.0)), g.findAt((12.5, 0.0)), g.findAt((6.25, 6.0))))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.8381, 
    farPlane=60.1571, width=46.5931, height=22.2561, cameraPosition=(21.0009, 
    7.55143, 52.4976), cameraTarget=(21.0009, 7.55143, 0))
p = mdb.models['draw-spline-sketch'].Part(name='waves', 
    dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p = mdb.models['draw-spline-sketch'].parts['waves']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['draw-spline-sketch'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['draw-spline-sketch'].sketches['__profile__']
del mdb.models['draw-spline-sketch'].parts['waves']
cliCommand("""# creating a sketch with a spline""")
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""import numpy as np""")
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,
        		                 recoverGeometry=COORDINATE)""")
cliCommand("""# Model parameters (N-mm-s)""")
cliCommand("""# ------------------------------------------------------------------""")
cliCommand("""model_name = 'waves-part-selection'""")
cliCommand("""b, h, ampl = 25., 6., 2.""")
cliCommand("""n_periods = 8.""")
cliCommand("""n_points = 80""")
cliCommand("""# Recreating model and calling it model_name""")
cliCommand("""Mdb()""")
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: mdb
cliCommand("""mdb.models.changeKey(fromName='Model-1', toName=model_name)""")
\
    cliCommand("""model = mdb.models[model_name]""")
cliCommand("""# obtain an equidistant array of points""")
cliCommand("""x_arr = np.linspace(0,b,n_points+1)""")
cliCommand("""# factor C in sin(C*x):""")
cliCommand("""# C*b = n_periods*pi""")
cliCommand("""y_arr = h + ampl * np.sin(x_arr*np.pi/b*n_periods) # *??""")
cliCommand("""# stack the x- and y arrays into one array""")
cliCommand("""spline_points = np.column_stack((x_arr,y_arr))""")
cliCommand("""# create stetch for part""")
cliCommand("""s = model.ConstrainedSketch(name='waves', sheetSize=200.0)""")
cliCommand("""# drawing the lower lines""")
cliCommand("""s.Line(point1=(0,0), point2=(0,h))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((0.0, 3.0),)
cliCommand("""s.Line(point1=(b,0), point2=(b,h))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((25.0, 3.0),)
cliCommand("""s.Line(point1=(0,0), point2=(b,0))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((12.5, 0.0),)
cliCommand("""# drawing the spline from points above""")
cliCommand("""s.Spline(points=(tuple(i) for i in spline_points))""")
#* TypeError: points; found 'generator', expecting a recognized type filling 
#* string dict
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
cliCommand("""(tuple(i) for i in spline_points)""")
#: <generator object <genexpr> at 0x000001921F766240>
cliCommand("""spline_points""")
#: array([[0.0, 6.0], [0.3125, 6.61803398874989], [0.625, 7.17557050458495], [0.9375, 7.61803398874989], [1.25, 7.90211303259031], [1.5625, 8.0], [1.875, 7.90211303259031], [2.1875, 7.61803398874989], [2.5, 7.17557050458495], [2.8125, 6.61803398874989], [3.125, 6.0], [3.4375, 5.38196601125011], [3.75, 4.82442949541506], [4.0625, 4.38196601125011], [4.375, 4.09788696740969], [4.6875, 4.0], [5.0, 4.09788696740969], [5.3125, 4.38196601125011], [5.625, 4.82442949541505], [5.9375, 5.38196601125011], [6.25, 6.0], [6.5625, 6.61803398874989], [6.875, 7.17557050458495], [7.1875, 7.6180339887499], [7.5, 7.90211303259031], [7.8125, 8.0], [8.125, 7.90211303259031], [8.4375, 7.61803398874989], [8.75, 7.17557050458495], [9.0625, 6.6180339887499], [9.375, 6.0], [9.6875, 5.38196601125011], [10.0, 4.82442949541505], [10.3125, 4.38196601125011], [10.625, 4.09788696740969], [10.9375, 4.0], [11.25, 4.09788696740969], [11.5625, 4.38196601125011], [11.875, 4.82442949541505], [12.1875, 5.3819660112501], [12.5, 6.0], [12.8125, 6.61803398874989], [13.125, 7.17557050458494], [13.4375, 7.61803398874989], [13.75, 7.90211303259031], [14.0625, 8.0], [14.375, 7.90211303259031], [14.6875, 7.6180339887499], [15.0, 7.17557050458495], [15.3125, 6.6180339887499], [15.625, 6.0], [15.9375, 5.3819660112501], [16.25, 4.82442949541506], [16.5625, 4.3819660112501], [16.875, 4.09788696740969], [17.1875, 4.0], [17.5, 4.09788696740969], [17.8125, 4.38196601125011], [18.125, 4.82442949541505], [18.4375, 5.38196601125011], [18.75, 6.0], [19.0625, 6.6180339887499], [19.375, 7.17557050458494], [19.6875, 7.6180339887499], [20.0, 7.90211303259031], [20.3125, 8.0], [20.625, 7.90211303259031], [20.9375, 7.6180339887499], [21.25, 7.17557050458495], [21.5625, 6.61803398874989], [21.875, 6.00000000000001], [22.1875, 5.38196601125011], [22.5, 4.82442949541506], [22.8125, 4.3819660112501], [23.125, 4.09788696740969], [23.4375, 4.0], [23.75, 4.09788696740969], [24.0625, 4.38196601125011], [24.375, 4.82442949541505], [24.6875, 5.3819660112501], [25.0, 6.0]], 'd')
cliCommand("""tuple((tuple(i) for i in spline_points))""")
#: ((0.0, 6.0), (0.3125, 6.618033988749895), (0.625, 7.175570504584947), (0.9375, 7.618033988749895), (1.25, 7.902113032590307), (1.5625, 8.0), (1.875, 7.902113032590307), (2.1875, 7.618033988749895), (2.5, 7.175570504584947), (2.8125, 6.618033988749895), (3.125, 6.0), (3.4375, 5.381966011250105), (3.75, 4.824429495415055), (4.0625, 4.381966011250105), (4.375, 4.097886967409693), (4.6875, 4.0), (5.0, 4.097886967409693), (5.3125, 4.381966011250105), (5.625, 4.824429495415053), (5.9375, 5.381966011250105), (6.25, 5.999999999999999), (6.5625, 6.618033988749894), (6.875, 7.175570504584946), (7.1875, 7.618033988749896), (7.5, 7.902113032590306), (7.8125, 8.0), (8.125, 7.902113032590307), (8.4375, 7.618033988749895), (8.75, 7.175570504584947), (9.0625, 6.618033988749896), (9.375, 6.000000000000001), (9.6875, 5.381966011250106), (10.0, 4.824429495415054), (10.3125, 4.381966011250108), (10.625, 4.097886967409693), (10.9375, 4.0), (11.25, 4.097886967409693), (11.5625, 4.381966011250105), (11.875, 4.824429495415053), (12.1875, 5.381966011250104), (12.5, 5.999999999999999), (12.8125, 6.618033988749894), (13.125, 7.175570504584945), (13.4375, 7.618033988749894), (13.75, 7.902113032590307), (14.0625, 8.0), (14.375, 7.902113032590306), (14.6875, 7.618033988749896), (15.0, 7.17557050458495), (15.3125, 6.618033988749896), (15.625, 6.000000000000004), (15.9375, 5.381966011250103), (16.25, 4.824429495415055), (16.5625, 4.381966011250103), (16.875, 4.097886967409693), (17.1875, 4.0), (17.5, 4.097886967409693), (17.8125, 4.381966011250107), (18.125, 4.824429495415052), (18.4375, 5.381966011250107), (18.75, 5.999999999999998), (19.0625, 6.618033988749897), (19.375, 7.175570504584945), (19.6875, 7.618033988749896), (20.0, 7.902113032590306), (20.3125, 8.0), (20.625, 7.90211303259031), (20.9375, 7.6180339887498985), (21.25, 7.175570504584948), (21.5625, 6.618033988749893), (21.875, 6.000000000000009), (22.1875, 5.38196601125011), (22.5, 4.824429495415055), (22.8125, 4.381966011250104), (23.125, 4.097886967409694), (23.4375, 4.0), (23.75, 4.097886967409693), (24.0625, 4.381966011250106), (24.375, 4.824429495415052), (24.6875, 5.3819660112501), (25.0, 5.999999999999998))
cliCommand("""tuple((tuple(i) for i in spline_points))""")
#: ((0.0, 6.0), (0.3125, 6.618033988749895), (0.625, 7.175570504584947), (0.9375, 7.618033988749895), (1.25, 7.902113032590307), (1.5625, 8.0), (1.875, 7.902113032590307), (2.1875, 7.618033988749895), (2.5, 7.175570504584947), (2.8125, 6.618033988749895), (3.125, 6.0), (3.4375, 5.381966011250105), (3.75, 4.824429495415055), (4.0625, 4.381966011250105), (4.375, 4.097886967409693), (4.6875, 4.0), (5.0, 4.097886967409693), (5.3125, 4.381966011250105), (5.625, 4.824429495415053), (5.9375, 5.381966011250105), (6.25, 5.999999999999999), (6.5625, 6.618033988749894), (6.875, 7.175570504584946), (7.1875, 7.618033988749896), (7.5, 7.902113032590306), (7.8125, 8.0), (8.125, 7.902113032590307), (8.4375, 7.618033988749895), (8.75, 7.175570504584947), (9.0625, 6.618033988749896), (9.375, 6.000000000000001), (9.6875, 5.381966011250106), (10.0, 4.824429495415054), (10.3125, 4.381966011250108), (10.625, 4.097886967409693), (10.9375, 4.0), (11.25, 4.097886967409693), (11.5625, 4.381966011250105), (11.875, 4.824429495415053), (12.1875, 5.381966011250104), (12.5, 5.999999999999999), (12.8125, 6.618033988749894), (13.125, 7.175570504584945), (13.4375, 7.618033988749894), (13.75, 7.902113032590307), (14.0625, 8.0), (14.375, 7.902113032590306), (14.6875, 7.618033988749896), (15.0, 7.17557050458495), (15.3125, 6.618033988749896), (15.625, 6.000000000000004), (15.9375, 5.381966011250103), (16.25, 4.824429495415055), (16.5625, 4.381966011250103), (16.875, 4.097886967409693), (17.1875, 4.0), (17.5, 4.097886967409693), (17.8125, 4.381966011250107), (18.125, 4.824429495415052), (18.4375, 5.381966011250107), (18.75, 5.999999999999998), (19.0625, 6.618033988749897), (19.375, 7.175570504584945), (19.6875, 7.618033988749896), (20.0, 7.902113032590306), (20.3125, 8.0), (20.625, 7.90211303259031), (20.9375, 7.6180339887498985), (21.25, 7.175570504584948), (21.5625, 6.618033988749893), (21.875, 6.000000000000009), (22.1875, 5.38196601125011), (22.5, 4.824429495415055), (22.8125, 4.381966011250104), (23.125, 4.097886967409694), (23.4375, 4.0), (23.75, 4.097886967409693), (24.0625, 4.381966011250106), (24.375, 4.824429495415052), (24.6875, 5.3819660112501), (25.0, 5.999999999999998))
cliCommand("""# creating a sketch with a spline""")
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""import numpy as np""")
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,
        		                 recoverGeometry=COORDINATE)""")
cliCommand("""# Model parameters (N-mm-s)""")
cliCommand("""# ------------------------------------------------------------------""")
cliCommand("""model_name = 'waves-part-selection'""")
cliCommand("""b, h, ampl = 25., 6., 2.""")
cliCommand("""n_periods = 8.""")
cliCommand("""n_points = 80""")
cliCommand("""# Recreating model and calling it model_name""")
cliCommand("""Mdb()""")
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: mdb
cliCommand("""mdb.models.changeKey(fromName='Model-1', toName=model_name)""")
\
    cliCommand("""model = mdb.models[model_name]""")
cliCommand("""# obtain an equidistant array of points""")
cliCommand("""x_arr = np.linspace(0,b,n_points+1)""")
cliCommand("""# factor C in sin(C*x):""")
cliCommand("""# C*b = n_periods*pi""")
cliCommand("""y_arr = h + ampl * np.sin(x_arr*np.pi/b*n_periods) # *??""")
cliCommand("""# stack the x- and y arrays into one array""")
cliCommand("""spline_points = np.column_stack((x_arr,y_arr))""")
cliCommand("""# create stetch for part""")
cliCommand("""s = model.ConstrainedSketch(name='waves', sheetSize=200.0)""")
cliCommand("""# drawing the lower lines""")
cliCommand("""s.Line(point1=(0,0), point2=(0,h))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((0.0, 3.0),)
cliCommand("""s.Line(point1=(b,0), point2=(b,h))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((25.0, 3.0),)
cliCommand("""s.Line(point1=(0,0), point2=(b,0))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((12.5, 0.0),)
cliCommand("""# drawing the spline from points above""")
cliCommand("""s.Spline(points=tuple((tuple(i) for i in spline_points)))""")
#: mdb.models['waves-part-selection'].sketches['waves'].geometry.findAt((6.25, 6.0),)
cliCommand("""# create part from sketch""")
cliCommand("""p = model.Part(name='waves', dimensionality=TWO_D_PLANAR,
               type=DEFORMABLE_BODY)""")
cliCommand("""p.BaseShell(sketch=s)""")
#: mdb.models['waves-part-selection'].parts['waves'].features['Shell planar-1']
p = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['waves-part-selection'].ConstrainedSketch(name='__edit__', 
    objectToCopy=mdb.models['waves-part-selection'].sketches['waves'])
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.6138, 
    farPlane=57.3814, width=33.6216, height=16.06, cameraPosition=(15.6998, 
    4.99884, 52.4976), cameraTarget=(15.6998, 4.99884, 0))
s.unsetPrimaryObject()
del mdb.models['waves-part-selection'].sketches['__edit__']
p = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: Coordinates of vertex 0 :0.,0.,0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.2065, 
    farPlane=57.8383, width=32.5973, height=13.5684, viewOffsetX=1.88309, 
    viewOffsetY=0.377616)
cliCommand("""p""")
#: mdb.models['waves-part-selection'].parts['waves']
cliCommand("""p.Set(name='all', faces=p.faces[:])""")
#: mdb.models['waves-part-selection'].parts['waves'].sets['all']
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
cliCommand("""p.edges.getByBoundingBox(xMax=1e-4)""")
#: mdb.models['waves-part-selection'].parts['waves'].edges.findAt(((0.0, 1.5, 0.0),),)
cliCommand("""p.Set(name='xsym', edges=p.edges.getByBoundingBox(xMax=1e-4))""")
#: mdb.models['waves-part-selection'].parts['waves'].sets['xsym']
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.7007, 
    farPlane=63.3441, width=34.0918, height=13.3337, viewOffsetX=2.3986, 
    viewOffsetY=0.466356)
p = mdb.models['waves-part-selection'].parts['waves']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(14.16679, 7.948954, 
    0.0), normal=(0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, origin=(14.279069, 
    2.817429, 0.0))
s1 = mdb.models['waves-part-selection'].ConstrainedSketch(name='__profile__', 
    sheetSize=52.49, gridSpacing=1.31, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['waves-part-selection'].parts['waves']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.5547, 
    farPlane=64.4406, width=38.0507, height=14.8821, cameraPosition=(11.4344, 
    3.9075, 52.4976), cameraTarget=(11.4344, 3.9075, 0))
s1.Line(point1=(-14.279069, 3.182571), point2=(10.720931, 3.182571))
s1.HorizontalConstraint(entity=g.findAt((-13.029069, 3.182571)), 
    addUndoState=False)
p = mdb.models['waves-part-selection'].parts['waves']
f = p.faces
pickedFaces = f.findAt(((14.16679, 7.948954, 0.0), ))
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['waves-part-selection'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.1733, 
    farPlane=62.8715, width=32.4095, height=12.6758, viewOffsetX=1.99513, 
    viewOffsetY=0.557369)
p = mdb.models['waves-part-selection'].parts['waves']
del p.features['Partition face-1']
cliCommand("""p.edges[0].featureName""")
#: 'Shell planar-1'
cliCommand("""p.edges[0].getAdjacentEdges()""")
#: mdb.models['waves-part-selection'].parts['waves'].edges.findAt(((0.0, 1.5, 0.0),),((25.0, 1.5, 0.0),),)
cliCommand("""p.edges[0].getCurvature()""")
#* TypeError: not all required arguments specified; expected 1, got 0
cliCommand("""p.edges[0].getFaces()""")
#: (0,)
cliCommand("""p.edges[0].getSize()""")
#: Length of edge = 25
#: 25.0
cliCommand("""p.edges[0].pointOn""")
#: ((6.25, 0.0, 0.0),)
cliCommand("""p.edges[1].getSize()""")
#: Length of edge = 6
#: 6.0
cliCommand("""p.edges[2].getSize()""")
#: Length of edge = 42.076612603333
#: 42.076612603333
cliCommand("""p.edges[3].getSize()""")
#: Length of edge = 6
#: 6.0
cliCommand("""p.edges[4].getSize()""")
#* IndexError: Sequence index out of range
cliCommand("""for edge in p.edges:
    print(edge)
    print(edge.getSize())
""")
#: ({'featureName': 'Shell planar-1', 'index': 0, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((6.25, 0.0, 0.0),)})
#: Length of edge = 25
#: 25.0
#: ({'featureName': 'Shell planar-1', 'index': 1, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((25.0, 1.5, 0.0),)})
#: Length of edge = 6
#: 6.0
#: ({'featureName': 'Shell planar-1', 'index': 2, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((6.25, 6.0, 0.0),)})
#: Length of edge = 42.076612603333
#: 42.0766126033
#: ({'featureName': 'Shell planar-1', 'index': 3, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((0.0, 1.5, 0.0),)})
#: Length of edge = 6
#: 6.0
cliCommand("""max_size = -1""")
cliCommand("""for edge in p.edges:
    print(edge)
    if edge.getSize() > max_size:
       lonest_edge = edge
       max_size = edge.getSize()
""")
#: ({'featureName': 'Shell planar-1', 'index': 0, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((6.25, 0.0, 0.0),)})
#: Length of edge = 25
#: Length of edge = 25
#: ({'featureName': 'Shell planar-1', 'index': 1, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((25.0, 1.5, 0.0),)})
#: Length of edge = 6
#: ({'featureName': 'Shell planar-1', 'index': 2, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((6.25, 6.0, 0.0),)})
#: Length of edge = 42.076612603333
#: Length of edge = 42.076612603333
#: ({'featureName': 'Shell planar-1', 'index': 3, 'instanceName': None, 'isReferenceRep': False, 'pointOn': ((0.0, 1.5, 0.0),)})
#: Length of edge = 6
cliCommand("""lonest_edge""")
#: mdb.models['waves-part-selection'].parts['waves'].edges.findAt((6.25, 6.0, 0.0),)
cliCommand("""lonest_edge.getBoundingBox()""")
#* AttributeError: 'Edge' object has no attribute 'getBoundingBox'
cliCommand("""lonest_edge""")
#: mdb.models['waves-part-selection'].parts['waves'].edges.findAt((6.25, 6.0, 0.0),)
cliCommand("""i_longest = lonest_edge.index""")
cliCommand("""i_longest""")
#: 2
cliCommand("""p.edges[i_longest]""")
#: mdb.models['waves-part-selection'].parts['waves'].edges.findAt((6.25, 6.0, 0.0),)
cliCommand("""p.edges[i_longest:i_longest+1]""")
#: mdb.models['waves-part-selection'].parts['waves'].edges.findAt(((6.25, 6.0, 0.0),),)
cliCommand("""p.Set(name='wave', edges=p.edges[i_longest:i_longest+1])""")
#: mdb.models['waves-part-selection'].parts['waves'].sets['wave']
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35.7111, 
    farPlane=69.3337, width=22.7941, height=16.1819, viewOffsetX=1.94961, 
    viewOffsetY=-0.0206742)
a=mdb.models['waves-part-selection'].parts['waves']
a.SetByBoolean(name='Set-4', operation=DIFFERENCE, sets=(a.sets['all'], 
    a.sets['wave'], ))
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a=mdb.models['waves-part-selection'].parts['waves']
a.SetByBoolean(name='Set-5', sets=(a.sets['wave'], a.sets['xsym'], ))
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['waves-part-selection'].parts['waves']
f = p.faces
faces = f.findAt(((14.16679, 7.948954, 0.0), ))
p.Set(faces=faces, name='Set-4')
#: The set 'Set-4' has been edited (1 face).
mdb.models['waves-part-selection'].parts['waves'].deleteSets(setNames=('Set-4', 
    'Set-5', ))
a = mdb.models['waves-part-selection'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['waves-part-selection'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
p1 = mdb.models['waves-part-selection'].parts['waves']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(width=22.4771, height=15.2112, 
    viewOffsetX=1.51387, viewOffsetY=-0.0989752)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35.4458, 
    farPlane=69.599, width=22.3097, height=15.1451, viewOffsetX=-0.0141201, 
    viewOffsetY=1.34574)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['waves-part-selection'].parts['waves']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
p = mdb.models['waves-part-selection'].parts['waves']
r = p.referencePoints
refPoints=(r[9], )
p.Set(referencePoints=refPoints, name='RP')
#: The set 'RP' has been created (1 reference point).
session.viewports['Viewport: 1'].view.setValues(nearPlane=34.7735, 
    farPlane=70.2713, width=42.9679, height=13.1284, viewOffsetX=-2.82656, 
    viewOffsetY=1.13764)
p = mdb.models['waves-part-selection'].parts['waves']
p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=3.0)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
p = mdb.models['waves-part-selection'].parts['waves']
f = p.faces
pickedFaces = f.findAt(((14.16679, 7.948954, 0.0), ))
d1 = p.datums
p.PartitionFaceByDatumPlane(datumPlane=d1[11], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4935, 
    farPlane=86.5513, width=73.4487, height=29.0098, cameraPosition=(8.67108, 
    6.27467, 52.5224), cameraTarget=(8.67108, 6.27467, 7.62939e-06))
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.5099, 
    farPlane=90.2091, cameraPosition=(4.86666, 19.316, 50.7351), 
    cameraUpVector=(-0.0814664, 0.963806, -0.253852), cameraTarget=(8.67108, 
    6.27467, 7.51019e-06))
session.viewports['Viewport: 1'].view.setValues(nearPlane=24.9328, 
    farPlane=81.7862, width=42.0857, height=16.6224, cameraPosition=(10.4856, 
    16.5513, 51.8671), cameraTarget=(14.2901, 3.50994, 1.13202))
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.2388, 
    farPlane=80.8062, cameraPosition=(16.7619, 20.1724, 50.8883), 
    cameraUpVector=(-0.0489746, 0.948158, -0.314004), cameraTarget=(14.3885, 
    3.56675, 1.11667))
session.viewports['Viewport: 1'].view.setValues(nearPlane=25.4498, 
    farPlane=81.5952, width=47.6298, height=18.8122, cameraPosition=(18.7812, 
    19.6752, 50.9579), cameraTarget=(16.4078, 3.06953, 1.18627))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['waves-part-selection'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(8.69062519073486, 
    -6.92777252197266))
session.viewports['Viewport: 1'].setValues(origin=(1.28750002384186, 
    -4.34999847412109))
session.viewports['Viewport: 1'].setValues(width=90.7687530517578)
session.viewports['Viewport: 1'].setValues(origin=(14.6453123092651, 
    -0.805557250976563))
session.viewports['Viewport: 1'].maximize()
