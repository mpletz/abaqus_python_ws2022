# first abq model of Abaqus/Python coarse

from abaqus import *
from abaqusConstants import *
from caeModules import *

session.journalOptions.setValues(replayGeometry=COORDINATE,
        		                 recoverGeometry=COORDINATE)

# Model parameters (N-mm-s)
# ------------------------------------------------------------------
model_name = 'first-abq-py-model'
b, h, t = 25., 50., 5.
r = 0.5

# Recreating model and calling it model_name
Mdb()
mdb.models.changeKey(fromName='Model-1', toName=model_name)
model = mdb.models[model_name]

# create stetch for part
s = model.ConstrainedSketch(name='rectangular', sheetSize=200.0)

# draw rectangle
s.rectangle(point1=(0,0), point2=(b,h))

# for loop for creating multile circles
for i in range(20):
    s.CircleByCenterPerimeter(center=(b/2.,4+i*2),
                              point1=(b/2.+r,4+i*2))

# create part and extrude sketch by t
p = model.Part(dimensionality=THREE_D, name='Plate',
               type=DEFORMABLE_BODY)
p.BaseSolidExtrude(depth=t, sketch=s)

# save the model as an .cae file
mdb.saveAs(model_name)