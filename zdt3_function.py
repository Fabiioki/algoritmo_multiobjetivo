# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:37:19 2023

@author: fabio
"""
import math
import random

def funcion_zdt3(x_real):
    # Función que devuelve el valor de f1(x) y f(x), siendo x un individuo de tamaño 30    
    n = len(x_real)
    tmp = 0.0
    for i in range(n):
        tmp += x_real[i]
        
    g = 1 + ((9*tmp)/(n-1))
    h = 1-math.sqrt(x_real[0]/g)-(x_real[0]/g)*math.sin(10*math.pi*x_real[0])
    obj = (x_real[0],g*h)
    return(obj) 


individuo = [random.random() for _ in range(30)]
zdt3_individuo = funcion_zdt3(individuo)

print(individuo)
print(zdt3_individuo)