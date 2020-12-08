#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:50:01 2020

@author: nautica
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# se tomaron 3 muestras de cada planta
# se asume que las plantas que se encuentran en cada columna fueron regadas de la misma forma
# posteriormente se deben tomar muestras basadas en la segmentación y mas de un solo pixel
# bien regadas
# las coordenadas se obtuvieron usando matplotlib
plantas_left=[[166,35],[186,73],[219,49],[136,145],[135,138],[160,105],[149,230],[138,149],[149,305]]
# regadas suficientemente
plantas_center=[[336,86],[351,129],[283,155],[323,271],[340,230],[291,245],[274,156],[307,66],[192,136]]
# mal regadas
plantas_right=[[505,95],[487,51],[543,30],[556,235],[525,214],[490,239],[451,300],[469,349],[540,343]]
muestras=[]
renglon=[]
columna=[]
distancia=[]
tiempo=[]
etiqueta=[]
for t in range(73):
    img=cv.imread('/home/nautica/Documents/investigacion/images/estres/Profuda'+str(t)+'.jpg',0)
    for col,ren in plantas_left:
        renglon.append(ren)
        columna.append(col)
        distancia.append(img[ren,col])
        tiempo.append(t)
        etiqueta.append('bien regada')
    for col,ren in plantas_center:
        renglon.append(ren)
        columna.append(col)
        distancia.append(img[ren,col])
        tiempo.append(t)
        etiqueta.append('regada suficiente')
    for col,ren in plantas_right:
        renglon.append(ren)
        columna.append(col)
        distancia.append(img[ren,col])
        tiempo.append(t)
        etiqueta.append('mal regada')
df = pd.DataFrame(list(zip(renglon, columna,distancia,tiempo,etiqueta)), columns =['renglon', 'columna','distancia','tiempo','etiqueta'])
print(df.head())
# verifica si la altura cambia en el trancurso de un dia para el punto 166,35
variacion_altura_al_dia=df[(df['renglon']==35)&(df['columna']==166)]
variacion_altura_al_dia.plot(x="tiempo", y=["distancia"])
#cv.imshow('imagen de profundidad',img)
#k = cv.waitKey(0)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()