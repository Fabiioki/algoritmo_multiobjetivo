# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:09:13 2023

@author: fabio
"""
import random

from pesos import crear_pesos, vecindad_pesos
from tchebycheff import tchebycheff, inicializar_punto_referencia, actualizar_punto_referencia
from zdt3_function import funcion_zdt3

N_poblacion = 40
T_vecindad = 0.2

##############################################################################################################
# INICIALIZACION

#---------------------------------------------------------
# Crear N vectores peso, uno por cada subproblema
Conjunto_pesos = crear_pesos(N_poblacion)
# print(Conjunto_pesos)
# print(len(Conjunto_pesos))
#---------------------------------------------------------


# Conjunto B(i) para cada vector peso calculamos sus T vectores vecinos 
Conjunto_pesos_vecinos = vecindad_pesos(Conjunto_pesos, T_vecindad)
# print(type(Conjunto_pesos_vecinos))
# for k,v in Conjunto_pesos_vecinos.items():
#     print("clave :", k)
#     print("vecinos: ",v)
#---------------------------------------------------------


# Inicializamos la población incial
def generacion_inicial(n_indivuos):
    # Crea tantos individuos como el parámetro que pasemos
    ls_individuos = list()
    
    for _ in range(n_indivuos):
        ls_individuos.append([random.random() for _ in range(30)])
        
    return ls_individuos

generacion_0 = generacion_inicial(N_poblacion)
# print(generacion_0)
#---------------------------------------------------------


# Evaluamos las prestaciones de la generación inicial
def test_generacion(individuos):
    puntos = list()
    for individuo in individuos:
        puntos.append(funcion_zdt3(individuo))
    return puntos

evaluacion_generacion_0 = test_generacion(generacion_0)
#---------------------------------------------------------


# Inicializamos los puntos de referencia (z1,z2):
punto_referencia_inicial = inicializar_punto_referencia(evaluacion_generacion_0)


################################################################################################################
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