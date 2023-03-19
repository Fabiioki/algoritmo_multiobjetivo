# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:49:06 2023

@author: Fabio
"""
from lectura_frente_ideal import Test_nsgaii, lista_frente
from main import puntos_finales

# ordenamos los puntos segun su x
pr_x,pr_y = (-0.5,-1)
ordenar_puntos = sorted(puntos_finales, key=lambda p: p[0])

# Imprimir la lista ordenada
print(ordenar_puntos)
print(len(ordenar_puntos))
res = 0

for x,y in ordenar_puntos:
    base = abs(pr_x - x)
    altura = abs(pr_y-y)
    res += base*altura
    pr_x = x

print(res)