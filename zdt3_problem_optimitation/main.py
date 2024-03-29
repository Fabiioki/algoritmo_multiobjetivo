# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:36:41 2023

@author: Fabio
"""
import random
import matplotlib.pyplot as plt

from tchebycheff import actualizar_punto_referencia , tchebycheff
from zdt3_function import funcion_zdt3
from inicializacion import generacion_inicial,crear_pesos, vecindad_pesos, test_generacion, inicializar_punto_referencia

# Parámetros de entrada establecidos:
    # N_poblacion: tamaño de la población
    # Generaciones: Número de generaciones
    # T_vecindad : Tamaño de vecindad
    
N_poblacion = 100
Generaciones = 100
T_vecindad = 0.20

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

############################################################################################################################################################################################################################

def comprobar_individuo(individuo):
    # comprobar que los valores del individuo sean aptos
    for i in range(len(individuo)):
        if individuo[i] < 0: individuo[i] = 0.0
        if individuo[i] > 1: individuo[i] = 1.0
    return individuo


def mutacion_DE(peso_subproblema, individuos_padres):
    factor_escala = random.uniform(0,2)
    # factor_escala = 0.5
    padre_1,padre_2,padre_3 = individuos_padres
    temp = [factor_escala*(p2-p3) for p2,p3 in zip(padre_2,padre_3)]
    vector_mutante = [ t+p1 for t,p1 in zip(temp,padre_1)] 
    return vector_mutante


def cruce_DE(individuo_mutante, individuo_subproblema):
    # Mezclar el individuo mutante con el individuo asignado al subproblema actual
    tasa_cruce = 0.5 # CR crossover constant
    individuo_resultado = [0.0]*30
    j = random.randint(0, 29) # indice elegido aleatoriamente -> esto hace que el hijo tenga al menos un parametro del vector mutante
    for i in range(30):
        if random.random() <= tasa_cruce or i == j:
            individuo_resultado[i] = individuo_mutante[i]
        else : 
            individuo_resultado[i] = individuo_subproblema[i]
    return individuo_resultado


def mutacion_gaussiana(individuo):
    # si aplicamos oiperador de mutacion gaussiana, lo aplicamos a cada componente de la solucion
    for it in range(len(individuo)): 
        individuo[it] = individuo[it] + random.uniform(0,0.05) # 0.05 porque sigma = (1-0)/20
    return individuo


def actualizacion_vecinos(hijo, punto_referencia, generacion_actual, peso_subproblema):
    # gte_hijo = tchebycheff(hijo, peso_subproblema, punto_referencia)
    indices_pesos_vecinos = Conjunto_pesos_vecinos[peso_subproblema]
    for indice_peso in indices_pesos_vecinos:
        peso = Conjunto_pesos[indice_peso]
        individuo = generacion_actual[indice_peso]
        gte_hijo = tchebycheff(hijo, peso, punto_referencia)
        gte_vecino = tchebycheff(individuo, peso, punto_referencia)
        if gte_hijo <= gte_vecino:
            generacion_actual[indice_peso] = hijo
    return generacion_actual

        

############################################################################################################################################################################################################################
def bucle(generacion_0, punto_referencia_inicial):
    generacion_actual = generacion_0.copy()
    punto_referencia_actual = punto_referencia_inicial
    it = 0
    for generacion in range(Generaciones):
        print("generacion:", it)
        for indice_subproblema in range(N_poblacion): 
            peso_subproblema = Conjunto_pesos[indice_subproblema] # obtenemos el peso del subproblema actual
            individuo_subproblema = generacion_actual[indice_subproblema] # obtenemos el individuo iesimo de la generacion actual (este es el individuo asignado a este subproblema)
            indices_pesos_mutacion = random.sample(Conjunto_pesos_vecinos[peso_subproblema], 3) # obtenemos los indices de los individuos para obtener el vector mutante
            individuos_mutacion = [generacion_actual[it] for it in indices_pesos_mutacion] # obtenemos los individuos iesimos para obtener el vector mutante            
            individuo_mutante = mutacion_DE(peso_subproblema, individuos_mutacion) # obtenemos el individuo mutante
            individuo_hijo = cruce_DE(individuo_mutante, individuo_subproblema) 
            if random.random() < 1/30:
                individuo_hijo = mutacion_gaussiana(individuo_hijo) # aplicamos el factor de mutuacion al hijo resultado                
            individuo_hijo = comprobar_individuo(individuo_hijo) # comprobamos que los valores del hijo estén dentro de los permintidos            
            evaluacion_hijo = funcion_zdt3(individuo_hijo) # evaluamos la funcion del hijo
            punto_referencia_actual = actualizar_punto_referencia(punto_referencia_actual, evaluacion_hijo) # actualizamos el punto de referencia
            generacion_actual = actualizacion_vecinos(individuo_hijo, punto_referencia_actual, generacion_actual, peso_subproblema) # cambiamos los individuos de los subproblemas vecinos
        it+=1
        '''
        puntos_finales = test_generacion(generacion_actual)
        p_x = [x[0] for x in puntos_finales]
        p_y = [y[1] for y in puntos_finales]
        plt.title("generacion: "+str(it))
        plt.scatter(p_x, p_y)
        # plt.scatter(peso_subproblema[0],peso_subproblema[1],color="red")
        plt.title("Punto referencia generacion "+str(it))
        plt.xlim(0, 1)
        plt.ylim(-1,4)
        plt.show()
        '''
    return generacion_actual


def visualizar_generacion_final():
    
    prueba_bucle = bucle(generacion_0, punto_referencia_inicial)
    puntos_finales = test_generacion(prueba_bucle)
    p_x = [x[0] for x in puntos_finales]
    p_y = [y[1] for y in puntos_finales]
    texto = "Número de subproblemas: "+ str(N_poblacion)+ ", Número de generaciones: "+ str(Generaciones) + ", Vecindad: " + str(T_vecindad)
    plt.title(texto)
    plt.scatter(p_x, p_y, color = "red")
    return puntos_finales

from lectura_frente_ideal import *
Generacion_final = visualizar_generacion_final()



#-------------------------------------------------------------------------------------------
# PLOTS ------------------------------------------------------------------------------------
# Visualizar los pesos vecinos de cada peso
def visualizar_vecinos_pesos():
    for peso in Conjunto_pesos:
        indices_pesos_vecinos = Conjunto_pesos_vecinos[peso]
        pesos_vecinos = [ Conjunto_pesos[peso] for peso in indices_pesos_vecinos]
        peso_x = [peso[0] for peso in pesos_vecinos]
        peso_y = [peso[1] for peso in pesos_vecinos]
        plt.scatter(peso_x, peso_y)
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.show()
        
# visualizar_vecinos_pesos()
#-------------------------------------------------------------------------------------------
# Visualizar todos los pesos en el plano
def visualizar_pesos():
    peso_x = [peso[0] for peso in Conjunto_pesos]
    peso_y = [peso[1] for peso in Conjunto_pesos]
    plt.scatter(peso_x, peso_y)
    
# visualizar_pesos()
#-------------------------------------------------------------------------------------------
# Visualizar el los individuos de la generacion incial sobre f1 y f2
def visualizar_gen_inicial_pr_inicial():
    puntos_gen_inicial = test_generacion(generacion_0)
    test_x = [x[0] for x in puntos_gen_inicial]
    test_y = [y[1] for y in puntos_gen_inicial]
    plt.title("PLot generación incial de "+ str(N_poblacion) + " individuos y punto de referencia inicial")
    plt.scatter(test_x, test_y)
    plt.scatter(punto_referencia_inicial[0], punto_referencia_inicial[1], color = "red")

# visualizar_gen_inicial_pr_inicial()