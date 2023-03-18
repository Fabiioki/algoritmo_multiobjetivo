# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:09:13 2023

@author: fabio
"""
import random
import matplotlib.pyplot as plt
import math

# from pesos import crear_pesos, vecindad_pesos
from tchebycheff import tchebycheff
from zdt3_function import funcion_zdt3

# N_poblacion = 100
# T_vecindad = 0.2

########################################################################################################################################################################
# INICIALIZACION

#------------------------------------------------------------------------------------------------------------------
# Crear N vectores peso, uno por cada subproblema
# Conjunto_pesos = crear_pesos(N_poblacion)
# print(Conjunto_pesos)
# print(len(Conjunto_pesos))
#------------------------------------------------------------------------------------------------------------------


# Conjunto B(i) para cada vector peso calculamos sus T vectores vecinos 
# Conjunto_pesos_vecinos = vecindad_pesos(Conjunto_pesos, T_vecindad)
# print(type(Conjunto_pesos_vecinos))
# for k,v in Conjunto_pesos_vecinos.items():
#     print("clave :", k)
#     print("vecinos: ",v)
#------------------------------------------------------------------------------------------------------------------

# Inicializamos la población incial
def generacion_inicial(n_indivuos):
    # Crea tantos individuos como el parámetro que pasemos
    ls_individuos = list()
    # n = math.trunc(n_indivuos/2)
    for _ in range(n_indivuos):
        ls_individuos.append([random.random() for _ in range(30)])
    
    # for _ in range(n_indivuos-n):
        # ls_individuos.append([random.uniform(0.5,1.0) for _ in range(30)])
    
    return ls_individuos

# generacion_0 = generacion_inicial(N_poblacion)
# print(generacion_0)
#------------------------------------------------------------------------------------------------------------------


# Evaluamos las prestaciones de la generación inicial
def test_generacion(individuos):
    puntos = list()
    for individuo in individuos:
        puntos.append(funcion_zdt3(individuo))
    return puntos

# evaluacion_generacion_0 = test_generacion(generacion_0)

########################################################################################################################################################################
# PESOS
def crear_pesos(N_pob):
    return  [(i/(N_pob-1), 1-i/(N_pob-1)) for i in range(N_pob)]

def distancia_vecinos(vector, vectores):
    # Dado un vector peso devuelve todas las distancias que tiene con los demas vectores peso
    def dist_euc (v1, v2):
        v1x,v1y = v1
        v2x,v2y = v2
        return math.sqrt((v2x-v1x)**2 + (v2y-v1y)**2)
    
    ls_out = list()
    for it in range(len(vectores)):
        ls_out.append((it, dist_euc(vector,vectores[it])))
    return ls_out

def vecindad_pesos(v_pesos,vecindad): # Devuelve los INDICES de los vecinos
    # Devuelve los vecinos más cercanos de un vector peso dado un porcentaje de vecinos que queremos
    # Clave = (vector_peso, puesto) : Valor = Conjunto de pesos vecinos
    vecinos = dict()
    n_vec = math.floor(vecindad*len(v_pesos))
    # it = 0
    for vector in v_pesos:
        aux = distancia_vecinos(vector,v_pesos)
        aux.sort(key = lambda x : x[1])
        vecinos_vector = aux[:n_vec]
        # vecinos[(vector,it)] = [v[0] for v in vecinos_vector]
        vecinos[(vector)] = [v[0] for v in vecinos_vector]
        # it += 1
    return vecinos


########################################################################################################################################################################
# Punto referencia 
def inicializar_punto_referencia(fitness_poblacion):
    conj_f1 = [fit[0] for fit in fitness_poblacion]
    conj_f2 = [fit[1] for fit in fitness_poblacion]
    return (min(conj_f1),min(conj_f2))

########################################################################################################################################################################
########################################################################################################################################################################═
# PRUEBAS 

# print(type(Conjunto_pesos_vecinos))
# for k,v in Conjunto_pesos_vecinos.items():
#     print("clave :", k)
#     print("vecinos: ",v)


# print("generacion 0",evaluacion_generacion_0)
# p_x = [x[0] for x in evaluacion_generacion_0]
# p_y = [y[1] for y in evaluacion_generacion_0]
# plt.scatter(p_x, p_y)


#print(z1_inicial,z2_inicial)

# Unir individuos con sus pesos
# lambda_individuos = list(zip(vector_pesos, generacion_0))
# print("vector pesos",lambda_individuos)