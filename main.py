# import math
import random
import matplotlib.pyplot as plt
# import numpy as np
import operator
# 
# from pesos import crear_pesos, vecindad_pesos
from tchebycheff import actualizar_punto_referencia , crear_pesos, tchebycheff, inicializar_punto_referencia
from zdt3_function import funcion_zdt3
from inicializacion import generacion_inicial, vecindad_pesos, test_generacion
# from cruce_DE import cruce_DE
from lectura_frente_ideal import *

# Parámetros de entrada establecidos:
    # N_poblacion: tamaño de la población
    # Generaciones: Número de generaciones
    # T_vecindad : Tamaño de vecindad
N_poblacion = 50
Generaciones = 200
T_vecindad = 0.10

# Pasos que hay que seguir:
    # Inicializacion
    # Acciones por iteracion (hasta condición de terminación):
        # Reproducción
        # Evaluación
        # Actualizar punto de referencia (z)
        # Actualización de vecinos

############################################################################################################################################################################################################################
# INICIALIZACION

# Crear N vectores peso, uno por cada subproblema
Conjunto_pesos = crear_pesos(N_poblacion)

# Conjunto B(i) para cada vector peso calculamos sus T vectores vecinos 
Conjunto_pesos_vecinos = vecindad_pesos(Conjunto_pesos, T_vecindad)

# Inicializamos la población incial
generacion_0 = generacion_inicial(N_poblacion)

# Evaluamos las prestaciones de la generación inicial
evaluacion_generacion_0 = test_generacion(generacion_0)

# Inicializamos los puntos de referencia (z1,z2):
punto_referencia_inicial = inicializar_punto_referencia(evaluacion_generacion_0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PRUEBAS:
# print("generacion 0",evaluacion_generacion_0)
# p_x = [x[0] for x in evaluacion_generacion_0]
# p_y = [y[1] for y in evaluacion_generacion_0]
# plt.scatter(p_x, p_y)

############################################################################################################################################################################################################################
# ITERACIONES
# Reproducción: Selecciona aleatoriamente índices de B(i) y genera una nueva solución "y" usando operadores evolutivos. (y = es hijo)
# Cruce DE : utilizamos 3 individuos elegidos aleatoriamente en la vecindad

# Evaluación: Evaluar F(y)

# Actualización del punto de referencia

# Actualización de vecinos

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_individuo_subproblema(generacion, peso, punto_referencia):
    
    diccionario_tchebycheff = dict()
    
    for individuo in generacion:
        diccionario_tchebycheff[tuple(individuo)] = tchebycheff(individuo, peso, punto_referencia)
    
    return min(diccionario_tchebycheff.items(), key = operator.itemgetter(1)) # Devuelve la clave y valor del valor mínimo del diccionario

# print(get_individuo_subproblema(generacion_0, Conjunto_pesos[1],punto_referencia_inicial))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mutacion_DE(peso_subproblema, generacion, punto_referencia):
    
    def get_individuos_padres(subproblemas_padres, generacion, punto_referencia):
        padres = list()
        for subproblema in subproblemas_padres:
            padre, _ = get_individuo_subproblema(generacion, subproblema, punto_referencia)
            padres.append(padre)
        return padres
    
    def comprobar_individuo(individuo):
        # comprobar que los valores del individuo sean aptos
        for i in range(len(individuo)):
            if individuo[i] < 0: individuo[i] = 0.
            if individuo[i] > 1: individuo[i] = 1.
        return individuo
    
    factor_escala = 0.5
    indices_subproblemas_padres = random.sample(Conjunto_pesos_vecinos[peso_subproblema], 3) # obtenemos los 3 subproblemas padres para la mutación
    subproblemas_padres = [Conjunto_pesos[i] for i in indices_subproblemas_padres ] 
    individuos_padres = get_individuos_padres(subproblemas_padres, generacion, punto_referencia)
    padre_1,padre_2,padre_3 = individuos_padres
    temp = [(p2-p3)*factor_escala for p2,p3 in zip(padre_2,padre_3)]
    hijo = [ t+p1 for t,p1 in zip(temp,padre_1) ] 
    return comprobar_individuo(hijo)

def cruce_DE(individuo_mutante, individuo_subproblema):
    tasa_cruce = 0.7
    individuo_resultado = [0.0]*30
    j = random.randint(0, 29)
    for i in range(30):
        if random.random() <= tasa_cruce or i == j:
            individuo_resultado[i] = individuo_mutante[i]
        else : 
            individuo_resultado[i] = individuo_subproblema[i]
    return individuo_resultado

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def actualizacion_vecinos(hijo, evaluacion_hijo ,peso_subproblema, punto_referencia, generacion):
    indices_pesos_vecinos = Conjunto_pesos_vecinos[peso_subproblema]
    gte_hijo = tchebycheff(hijo, peso_subproblema, punto_referencia)
    # print(hijo)
    # print("llego aquiiii:", gte_hijo)
    for indice_peso in indices_pesos_vecinos:
        peso = Conjunto_pesos[indice_peso]
        # print(peso,"pesooo")
        individuo,_ = get_individuo_subproblema(generacion, peso, punto_referencia)
        # print(individuo,"indivvv")
        gte_vecino = tchebycheff(list(individuo), peso, punto_referencia)
        if gte_hijo <= gte_vecino:
            generacion[indice_peso] = hijo
    return generacion

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bucle(generacion_0, punto_referencia_inicial):
    generacion_actual = generacion_0
    punto_referencia_actual = punto_referencia_inicial
    it = 0
    for generacion in range(Generaciones):
        print("generacion:", it)
        for indice_subproblema in range(N_poblacion):
            # if random.random() < 0.5 : 
            peso_subproblema = Conjunto_pesos[indice_subproblema]
            individuo_subproblema,_ = get_individuo_subproblema(generacion_actual, peso_subproblema, punto_referencia_actual)
            individuo_mutante = mutacion_DE(peso_subproblema, generacion_actual, punto_referencia_actual)
            individuo_hijo = cruce_DE(individuo_mutante, list(individuo_subproblema))
            evaluacion_hijo = funcion_zdt3(individuo_hijo)
            punto_referencia_actual = actualizar_punto_referencia(punto_referencia_actual, evaluacion_hijo)
            generacion_actual = actualizacion_vecinos(individuo_hijo, evaluacion_hijo, peso_subproblema, punto_referencia_actual, generacion_actual)
        it+=1
    
    return generacion_actual    

prueba_bucle = bucle(generacion_0, punto_referencia_inicial)
puntos_finales = test_generacion(prueba_bucle)
print(puntos_finales)
p_x = [x[0] for x in puntos_finales]
p_y = [y[1] for y in puntos_finales]
plt.scatter(p_x, p_y)




