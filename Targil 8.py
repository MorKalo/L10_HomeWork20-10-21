#כתוב פונקציה המקבלת רדיוס מעגל ומחזירה את היקף המעגל

import math

def getCircleHekef(radius):
    hekef=radius*2*math.pi
    return hekef

radius=float(input('plz enter thr radius of the circle:'))

print(f'the HEKEF of the circle that is radius is {radius} is {getCircleHekef(radius)}')