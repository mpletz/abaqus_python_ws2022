# cantilever beam: convert the json files from App to a dictionary of (x,y)-splines
# Android app: https://play.google.com/store/apps/details?id=mul.kkv.FEMon2
# Description: https://www.kunststofftechnik.at/fileadmin/shares/kunststofftechnik/lehrstuhl/Konstruieren_in_Kunst-_und_Verbundstoffen/Docs/FEMon.pdf

import numpy as np
import json, os
import matplotlib.pyplot as plt
from abaqus import *
from abaqusConstants import *
from caeModules import *

def get_profile(file_name,if_krag=0,if_mikro=0):
    # aktuelle koordinaten bekommen
    def get_coords(dict_geom,if_krag=0):
        if 'x' in dict_geom.keys() and 'y' in dict_geom.keys():
            if if_krag:
                #print((np.array(dict_geom['x'])==0.)*(np.array(dict_geom['y'])==0.))
                i0 = np.where((np.array(dict_geom['x'])==0.)*(np.array(dict_geom['y'])==0.))[0][0]
                #
                x = np.array(dict_geom['x'][i0+1:]+dict_geom['x'][:i0])
                y = -np.array(dict_geom['y'][i0+1:]+dict_geom['y'][:i0])
                #plt.plot(x,y)
                #plt.show()
                return np.column_stack((x,y))
            else:
                return np.column_stack((dict_geom['x'],[-i for i in dict_geom['y']]))
        else:
            return []
    # Profil aus json Datei laden und darstellen
    with open(file_name,'r') as f:
        inp = f.read()
    #
    geom = json.loads(inp)
    #
    aussen = geom['children'][0]
    innen = geom['children'][0]['children']
    #
    aussen_kontur = get_coords(aussen,if_krag)
    innen_konturen = []
    schicht_aktuell = innen
    while 1:
        len_aktuell = len(innen_konturen)
        for cont in schicht_aktuell:
            kont_temp = get_coords(cont,0)
            #plt.plot(kont_temp[:,0],kont_temp[:,1])
            innen_konturen += [kont_temp]
        if if_mikro:
            break
        if len(innen_konturen) == len_aktuell:
            break
        schicht_neu = []
        for k in schicht_aktuell:
            schicht_neu += k['children']
        schicht_aktuell = schicht_neu
    #plt.show()
    print(aussen_kontur,innen_konturen)
    return aussen_kontur,innen_konturen

# load json file and write to new, simple json
json_file = 'Sebastian.json'

b, h = 120., 40.

Mdb()
model = mdb.models['Model-1']

sketch=model.ConstrainedSketch(name='sketch0', sheetSize=200.0)
sketch.Line(point1=(0.0, 0.0), point2=(b, 0.0))
sketch.Line(point1=(0.0, 0.0), point2=(0.,-h))

spline_aussen, splines_i = get_profile(json_file,1)
spline_aussen = np.ascontiguousarray(spline_aussen)
splines_i = np.ascontiguousarray(splines_i)

sketch.Spline(points=spline_aussen)

if splines_i != []:
    for loch in splines_i:
        print(loch[0])
        sketch.Spline(points=list([list(i) for i in loch])+[list(loch[0])])

part=model.Part(dimensionality=TWO_D_PLANAR, name='Cantilever-beam',
                type=DEFORMABLE_BODY)

part.BaseShell(sketch=sketch)
mdb.saveAs('test-sketch')