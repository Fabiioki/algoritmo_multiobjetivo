# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:49:06 2023

@author: Fabio
"""
import matplotlib.pyplot as plt

from lectura_frente_ideal import Test_nsgaii, lista_frente
from main import Generacion_final

def hipervolumen(lista_puntos, punto_referencia):
    # ordenamos los puntos según su x
    lista_ordenada = sorted(lista_puntos, key=lambda p: p[0])
    pr_x,pr_y = punto_referencia
    
    res = 0
    for x,y in lista_ordenada:
        base = abs(pr_x - x)
        altura = abs(pr_y-y)
        res += base*altura
        pr_x = x
    return res

punto_referencia = (0,-1)
print("###########################################################################")
print("Hipervolumen de la generación final de nsgaii: " + str(hipervolumen(Test_nsgaii, punto_referencia)))
print("Hipervolumen de la generación final del algoritmo: " + str(hipervolumen(Generacion_final, punto_referencia)))


########################################################################################################################


def conjunto_cobertura(frente_1, frente_2):
    res = 0
    for p1_x, p1_y in frente_1:
        frente2_domina = False
        for p2_x, p2_y in frente_2:
            if (p2_x <= p1_x and p2_y <= p1_y) and (p2_x < p1_x or p2_y < p1_y):
               frente2_domina = True
               break
        if not frente2_domina:
            res+=1
    return res/len(frente_1)

print("--------------------------------------------------------------------")
print("Cobertura del algoritmo a nsgaii: "+str(conjunto_cobertura(Generacion_final, Test_nsgaii)))
print("Cobertura de nsgaii al algoritmo: " +str(conjunto_cobertura(Test_nsgaii,Generacion_final)))
print("###########################################################################")