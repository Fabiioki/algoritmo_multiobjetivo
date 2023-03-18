# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:37:19 2023

@author: fabio
"""
import math

def funcion_zdt3(x):
    # Función objetivo 1
    f1 = x[0]
    
    # Función objetivo 2
    g = 1 + 9 / (len(x) - 1) * sum(x[i] for i in range(1, len(x)))
    h = 1 - math.sqrt(f1 / g) - (f1 / g) * math.sin(10 * math.pi * f1)
    f2 = g * h
    
    return f1, f2
################################################################################################################
# PRUEBAS 

# individuo = [random.random() for _ in range(30)]
# zdt3_individuo = funcion_zdt3(individuo)

# print(individuo)
# print(zdt3_individuo)