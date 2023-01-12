# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
from caeModules import *


s = mdb.models['Model-1']
# I-Beam
Lb=3000 #long
Hs=300  #total height
Tfs=40  #upper flange height
Tfx=40  #downer flange height
Wss=250 #up width
Wsx=250 #down width
Tw=40
# Ribs
Wh=500 #width
Hh=260 #height
Lh=10 #length
# Stud
Sj=20  # body diameter
Sg=100 # body height
Mg=20 # head height
Mj=40  # head diameter



#control function
if Wsx<Wss:
    Ww=Wsx
else:
    Ww=Wss

if Wh>(Ww-Tw)/2:
    Wh=(Ww-Tw)/2
else:
    Wh=Wh

if Hh<Hs-Tfx-Tfs:
    Hh=Hh
else:
    Hh=Hs-Tfx-Tfs

Wdb = (Ww-Tw)/4+ Tw/2
Dlr = (Wdb / 2 + Tw / 2)



# main part H-Beam
s1=s.ConstrainedSketch(name='__profile__',
    sheetSize=1000.0)

xy=((0.0, 0.0),(Wsx/2, 0.0),(Wsx/2, Tfx),(Tw/2, Tfx),(Tw/2, Hs-Tfs),(Wss/2, Hs-Tfs),(Wss/2, Hs),(-Wss/2, Hs),
    (-Wss/2, Hs-Tfs),(-Tw/2, Hs-Tfs),(-Tw/2, Tfx),(-Wsx/2, Tfx),(-Wsx/2, 0.0),(0,0))
for i in range(len(xy)-1):
    s1.Line(point1=xy[i],point2=xy[i+1])

p = s.Part(name='S-Beam', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s1, depth=Lb)


# Trans
s2=s.ConstrainedSketch(name='TranStiffener-skech',sheetSize=1000)
xy=((0,Tfx),(Wh/2,Tfx),(Wh/2,Hh+Tfx),(-Wh/2,Hh+Tfx),(-Wh/2,Tfx),(0,Tfx))
for i in range(len(xy)-1):
    s2.Line(point1=xy[i],point2=xy[i+1])

Tran=s.Part(name='Tran', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
Tran.BaseSolidExtrude(sketch=s2, depth=Lh)


#Studs
st=s.ConstrainedSketch(name='Stud-skech',sheetSize=1000)
cline=st.ConstructionLine((0,15),(0,-15)) # reference line: y axis
xy=((0, Hs), (Sj/2, Hs), (Sj/2, Hs+Sg), (Mj/2, Hs+Sg), (Mj/2,Hs+Sg+Mg),(0, Hs+Sg+Mg), (0, Hs))
for i in range(len(xy)-1):
    st.Line(point1=xy[i],point2=xy[i+1])

Stud=s.Part(name='Stud',dimensionality=THREE_D, type=DEFORMABLE_BODY)
Stud.BaseSolidRevolve(sketch=st, angle=360, flipRevolveDirection=OFF)


# assembly
a = s.rootAssembly
## beams
part0101= a.Instance(name='S-Beam-1', part=p, dependent=ON)
part0102= a.Instance(name='S-Beam-2', part=p, dependent=ON)
part0102.translate(vector=(0,0,Lb))

# Rippen
part0201= a.Instance(name='Tran-1', part=Tran, dependent=ON)
part0202= a.Instance(name='Tran-2', part=Tran, dependent=ON)
part0203= a.Instance(name='Tran-3', part=Tran, dependent=ON)
part0204= a.Instance(name='Tran-4', part=Tran, dependent=ON)
part0205= a.Instance(name='Tran-5', part=Tran, dependent=ON)
part0206= a.Instance(name='Tran-6', part=Tran, dependent=ON)
part0201.translate(vector=(Ww/2-Wh/2,0,0))
part0202.translate(vector=(-Ww/2+Wh/2,0,0))
part0203.translate(vector=(Ww/2-Wh/2,0,Lb))
part0204.translate(vector=(-Ww/2+Wh/2,0,Lb))
part0205.translate(vector=(Ww/2-Wh/2,0,2*Lb))
part0206.translate(vector=(-Ww/2+Wh/2,0,2*Lb))


# assembly
#a = s.rootAssembly

#part0101= a.Instance(name='S-Beam-1', part=p, dependent=ON)
#part0102= a.Instance(name='S-Beam-2', part=p, dependent=ON)
#part0102.translate(vector=(0,0,3000))

#a = s.rootAssembly
#a.translate(instanceList=('S-Beam-2', ), vector=(0.0, 20.0, -3000.0))
#: The instance S-Beam-2 was translated by 0., 20., -3.E+03 with respect to the assembly coordinate system

#a = mdb.models['Model-1'].rootAssembly
#a.translate(instanceList=('S-Beam-2', ), vector=(0.0, -20.0, 0.0))
#: The instance S-Beam-2 was translated by 0., -20., 0. with respect to the assembly coordinate system

#a = mdb.models['Model-1'].rootAssembly
#p = mdb.models['Model-1'].parts['Tran']
#a.Instance(name='Tran-1', part=p, dependent=ON)

#a = mdb.models['Model-1'].rootAssembly
#a.translate(instanceList=('Tran-1', ), vector=(73.0, 0.0, 0.0))
#: The instance Tran-1 was translated by 73., 0., 0. with respect to the assembly coordinate system
#a = mdb.models['Model-1'].rootAssembly
#p = mdb.models['Model-1'].parts['Tran']
#a.Instance(name='Tran-2', part=p, dependent=ON)

#a = mdb.models['Model-1'].rootAssembly
#a.translate(instanceList=('Tran-2', ), vector=(73.0, 0.0, 0.0))
#: The instance Tran-2 was translated by 73., 0., 0. with respect to the assembly coordinate system
#a = mdb.models['Model-1'].rootAssembly
#a.translate(instanceList=('Tran-2', ), vector=(0.0, 0.0, -3000.0))
#: The instance Tran-2 was translated by 0., 0., -3.E+03 with respect to the assembly coordinate system