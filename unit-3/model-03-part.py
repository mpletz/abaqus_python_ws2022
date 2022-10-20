# creating a sketch with a spline

from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

session.journalOptions.setValues(replayGeometry=COORDINATE,
        		                 recoverGeometry=COORDINATE)
TOL = 1e-4

# Model parameters (N-mm-s)
# ------------------------------------------------------------------
model_name = 'waves-part-selection'
b, h, ampl = 25., 6., 2.
n_periods = 8.

n_points = 80

# Recreating model and calling it model_name
Mdb()
mdb.models.changeKey(fromName='Model-1', toName=model_name)
model = mdb.models[model_name]

# obtain an equidistant array of points
x_arr = np.linspace(0,b,n_points+1)

# factor C in sin(C*x):
# C*b = n_periods*pi
y_arr = h + ampl * np.sin(x_arr*np.pi/b*n_periods) # *??

# stack the x- and y arrays into one array
spline_points = np.column_stack((x_arr,y_arr))

# create stetch for part
s = model.ConstrainedSketch(name='waves', sheetSize=200.0)

# drawing the lower lines
s.Line(point1=(0,0), point2=(0,h))
s.Line(point1=(b,0), point2=(b,h))
s.Line(point1=(0,0), point2=(b,0))

# drawing the spline from points above
s.Spline(points=tuple((tuple(i) for i in spline_points)))

# create part from sketch
p = model.Part(name='waves', dimensionality=TWO_D_PLANAR,
               type=DEFORMABLE_BODY)
p.BaseShell(sketch=s)

# selecting stuff
p.Set(name='all', faces=p.faces[:])

# edge on left side via getByBoundingBox
p.Set(name='xsym', edges=p.edges.getByBoundingBox(xMax=TOL))

# Top edge as the longest edge
max_size = -1
for edge in p.edges:
     print(edge)
     if edge.getSize() > max_size:
        longest_edge = edge
        max_size = edge.getSize()

# to get the edge array of longest edge
i_longest = longest_edge.index
p.Set(name='wave', edges=p.edges[i_longest:i_longest+1])


