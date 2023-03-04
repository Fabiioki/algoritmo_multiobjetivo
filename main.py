import math
import random
import matplotlib.pyplot as plt
import numpy as np

from pesos import crear_pesos, vecindad_pesos
from tchebycheff import tchebycheff
from zdt3_function import funcion_zdt3


# Parámetros de entrada establecidos:
    # N_poblacion: tamaño de la población
    # Generaciones: Número de generaciones
    # T_vecindad : Tamaño de vecindad
N_poblacion = 30
Generaciones = 300
T_vecindad = 0.2

# Pasos que hay que seguir:
    # Inicializacion
    # Acciones por iteracion (hasta condición de terminación):
        # Reproducción
        # Evaluación
        # Actualizar punto de referencia (z)
        # Actualización de vecinos

##############################################################################################################
# INICIALIZACION
# Crear N vectores peso, uno por cada subproblema
vector_pesos = crear_pesos(N_poblacion)

# Conjunto B(i) para cada vector peso calculamos sus T vectores vecinos 
conjunto_pesos_vecinos = vecindad_pesos(vector_pesos, T_vecindad)

# Inicializamos la población incial
def generacion_inicial(n_indivuos):
    # Crea tantos individuos como el parámetro que pasemos
    ls_individuos = list()
    
    for _ in range(n_indivuos):
        ls_individuos.append([random.random() for _ in range(30)])
        
    return ls_individuos

generacion_0 = generacion_inicial(N_poblacion)

# Evaluamos las prestaciones de la generación inicial
def test_generacion(individuos):
    puntos = list()
    for individuo in individuos:
        puntos.append(funcion_zdt3(individuo))
    return puntos

evaluacion_generacion_0 = test_generacion(generacion_0)
print(evaluacion_generacion_0)

p_x = [x[0] for x in evaluacion_generacion_0]
p_y = [y[1] for y in evaluacion_generacion_0]
plt.scatter(p_x, p_y)

##############################################################################################################


### GENERACIÓN INICIAL






# puntos = test_generacion(generacion_inicial(30))
# print(puntos)

# p_x = [x[0] for x in puntos]
# #print(p_x)
# p_y = [y[1] for y in puntos]

# plt.scatter(p_x, p_y)



