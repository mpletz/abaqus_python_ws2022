# Axial-symmetric indenter model
# MP, 2021-11; adapted for Abaqus/Python course 2022-10

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os
import shutil
import numpy as np

DIR0 = os.path.abspath('')
TOL = 1e-4

odb_name = 'indenter-v2/indenter-pl'

def make_nice_image(odb_name):
    vp = session.viewports['Viewport: 1']

    vp.restore()
    vp.setValues(origin=(6, 160), width=130, height=70)

    # open the odb with the odb_name
    odb = session.openOdb(name=odb_name+'.odb')

    vp.setValues(displayedObject=odb)

    vp.viewportAnnotationOptions.setValues(triad=OFF, title=OFF, state=OFF,
                                        annotations=OFF, compass=OFF)

    vp.viewportAnnotationOptions.setValues(legendBackgroundStyle=MATCH,
                                        legendFont='-*-verdana-medium-r-normal-*-*-80-*-*-p-*-*-*')

    session.View(name='User-1', nearPlane=2.7153, farPlane=5.1208, width=1.65,
                height=0.79473, projection=PERSPECTIVE, cameraPosition=(0.5, -0.020711,
                                                                        3.918), cameraUpVector=(0, 1, 0), cameraTarget=(0.5, -0.020711, 0),
                viewOffsetX=-0.27334, viewOffsetY=0.031281, autoFit=OFF)

    vp.view.setValues(session.views['User-1'])

    vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ), )

    vp.odbDisplay.setPrimaryVariable(variableLabel='S',
                                    outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
                                    'Max. Principal'), )

    vp.odbDisplay.commonOptions.setValues(visibleEdges=FREE)

    session.pngOptions.setValues(imageSize=(20*130, 20*70))
    session.printOptions.setValues(vpDecorations=OFF, reduceColors=False)
    session.printToFile(fileName=odb_name+'-sI', format=PNG, canvasObjects=(vp, ))
    return

make_nice_image(odb_name)

