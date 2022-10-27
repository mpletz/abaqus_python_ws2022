# Axial-symmetric indenter model
# MP, 2021-11; adapted for Abaqus/Python course 2022-10

from abaqus import *
from abaqusConstants import *
import os, shutil
import numpy as np

DIR0 = os.path.abspath('')
TOL = 1e-4

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

odb_name = 'indenter-pl'

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
    np.savetxt(odb_name+'-res.dat',np.column_stack((u_list,rf_list)),header='U2 (mm), RF2 (N)',
               delimiter=', ')
    return

eval_fu_curve(odb_name)

#import matplotlib.pyplot as plt
#plt.plot(u_list,rf_list)
#plt.show()

"""
[-0.0, -0.01796642504632473, -0.03899382799863815, -0.05533164367079735, -0.08224976062774658, -0.11000345647335052, -0.15674972534179688, -0.2521131634712219, -0.40081197023391724, -0.6400505304336548, -1.06219482421875, -1.254154086112976, -1.493717074394226, -1.8197028636932373, -2.096626043319702, -2.5720884799957275, -3.261892318725586, -4.40778923034668, -4.763731002807617, -5.082640171051025, -5.5311970710754395, -6.2430338859558105, -7.33556604385376, -9.107773780822754, -11.058220863342285, -13.163244247436523, -15.530720710754395, -17.222454071044922, -17.222454071044922, -14.609292030334473, -12.070769309997559, -8.534492492675781, -3.801131010055542, -2.2839653491973877, -0.4215206205844879, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]"""