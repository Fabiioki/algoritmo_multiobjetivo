# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:13:50 2023

@author: fabio
"""

import math
import random
# PESOS

def crear_pesos(N_pob):
    return  [(i/(N_pob-1), 1-i/(N_pob-1)) for i in range(N_pob)]

def dist_euc (v1, v2):
    v1x,v1y = v1
    v2x,v2y = v2
    return math.sqrt((v2x-v1x)**2 + (v2y-v1y)**2)

def distancia_vecinos(vector, vectores):
    # Dado un vector peso devuelve todas las distancias que tiene con los demas vectores peso 
    ls_out = list()
    for vs in vectores:
        ls_out.append((vs, dist_euc(vector,vs)))
    return ls_out

def vecindad_pesos(v_pesos,vecindad):
    # Devuelve los vecinos más cercanos de un vector peso dado un porcentaje de vecinos que queremos
    vecinos = dict()
    n_vec = math.floor(vecindad*len(v_pesos))

    for vector in v_pesos:
        aux = distancia_vecinos(vector,v_pesos)
        aux.sort(key = lambda x : x[1])
        vecinos_vector = aux[:n_vec]
        vecinos[vector] = [v[0] for v in vecinos_vector]

    return vecinos


# PRUEBAS:
# N = 30
# vectores_peso =  [(i/(N-1), 1-i/(N-1)) for i in range(N)]
# # print(vectores_peso)
# vecindad = 0.20
# vecinos = vecindad_pesos(vectores_peso, vecindad)[(1.0, 0.0)]
# print(vecinos)
# print(random.sample(vecinos, 3))