# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:37:19 2023

@author: fabio
"""
import math
import random

# def funcion_zdt3(x_real):
#     # Función que devuelve el valor de f1(x) y f(x), siendo x un individuo de tamaño 30    
#     n = len(x_real)
#     tmp = 0.0
    
#     for i in range(1,n):
#         tmp += x_real[i]
        
#     g = 1 + ((9*tmp)/(n-1))
#     h = 1 - math.sqrt(x_real[0]/g) - (x_real[0]/g)*math.sin(10*math.pi*x_real[0])
#     obj = (x_real[0],g*h)
#     return(obj) 
def funcion_zdt3(x):
    # Función objetivo 1
    f1 = x[0]
    
    # Función objetivo 2
    g = 1 + 9 / (len(x) - 1) * sum(x[i] for i in range(1, len(x)))
    h = 1 - math.sqrt(f1 / g) - (f1 / g) * math.sin(10 * math.pi * f1)
    f2 = g * h
    
    return f1, f2
print(funcion_zdt3([0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.5538575234995294, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0]))
################################################################################################################
# PRUEBAS 

# individuo = [random.random() for _ in range(30)]
# zdt3_individuo = funcion_zdt3(individuo)

# print(individuo)
# print(zdt3_individuo)