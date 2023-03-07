import math
import random
import matplotlib.pyplot as plt
import numpy as np

from pesos import crear_pesos, vecindad_pesos
from tchebycheff import tchebycheff, inicializar_punto_referencia, actualizar_punto_referencia
from zdt3_function import funcion_zdt3
from inicializacion import generacion_inicial, test_generacion
from cruce_DE import cruce_DE

# Parámetros de entrada establecidos:
    # N_poblacion: tamaño de la población
    # Generaciones: Número de generaciones
    # T_vecindad : Tamaño de vecindad
N_poblacion = 40
Generaciones = 250
T_vecindad = 0.1

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
Conjunto_pesos = crear_pesos(N_poblacion)

# Conjunto B(i) para cada vector peso calculamos sus T vectores vecinos 
Conjunto_pesos_vecinos = vecindad_pesos(Conjunto_pesos, T_vecindad)

# Inicializamos la población incial
generacion_0 = generacion_inicial(N_poblacion)

# Evaluamos las prestaciones de la generación inicial
evaluacion_generacion_0 = test_generacion(generacion_0)

# Inicializamos los puntos de referencia (z1,z2):
punto_referencia_inicial = inicializar_punto_referencia(evaluacion_generacion_0)


##############################################################################################################
# ITERACIONES
# Reproducción: Selecciona aleatoriamente índices de B(i) y genera una nueva solución "y" usando operadores evolutivos. (y = es hijo)
# Cruce DE : utilizamos 3 individuos elegidos aleatoriamente en la vecindad

# peso_e, individuo_e = lambda_individuos[0]
# print("ejemplo : ", ex)

vecinos_prueba = Conjunto_pesos_vecinos[(0.0, 1.0)] #vecinos
hijo = cruce_DE(0, Conjunto_pesos, generacion_0, Conjunto_pesos_vecinos)
print("Hijo: ", hijo)
# print(len(hijo))

# Evaluación: Evaluar F(y)
# evaluacion_hijo = funcion_zdt3(hijo)
# print(evaluacion_hijo)

# Actualización del punto de referencia
# act_punto_referencia = actualizar_punto_referencia((z1_inicial, z2_inicial), evaluacion_hijo)
# print(act_punto_referencia)



# Actualización de vecinos
# def actualizacion_vecinos(peso, hijo, generacion ,punto_referencia):
#     def get_individuos_vecinos(pesos_vecinos,generacion):
#         res = list()
#         for peso in pesos_vecinos:
#             i = Vector_pesos.index(peso)
#             res.append(generacion[i])
#         return res
    
#     pesos_vecinos = Conjunto_pesos_vecinos[peso]
#     individuos_vecinos = get_individuos_vecinos(pesos_vecinos, generacion)
#     gte_hijo = tchebycheff(hijo, peso, punto_referencia)
#     for i in range(len(pesos_vecinos)):
#         gte_vecino = tchebycheff(individuos_vecinos[i],pesos_vecinos[i],punto_referencia)
#         if gte_hijo < gte_vecino:
#             puesto = Vector_pesos.index(pesos_vecinos[i])
#             generacion[puesto] = hijo
#             print("ha cambiado el elemento :", puesto)
#     return generacion
    
def actualizacion_vecinos(it_individuo, hijo, punto_referencia, pesos, generacion, pesos_vecinos):
    
    def get_candidatos(pesos, pesos_padres ,generacion):
        res = list()
        for peso_p in pesos_padres:
            indice = pesos.index(peso_p)
            res.append(generacion[indice])
        return res
    
    pesos_vecinos = pesos_vecinos[list(pesos_vecinos)[it_individuo]]
    individuos_vecinos = get_candidatos(pesos, pesos_vecinos, generacion)
    gte_hijo = tchebycheff(hijo, pesos[it_individuo], punto_referencia)
    
    for i in range(len(pesos_vecinos)):
        
        gte_vecino = tchebycheff(individuos_vecinos[i],pesos_vecinos[i],punto_referencia)
        if gte_hijo < gte_vecino:
            puesto = pesos.index(pesos_vecinos[i])
            print("El individuo ",puesto,"ha cambiado")
            generacion[puesto] = hijo
    return generacion

act_vecinos = actualizacion_vecinos(20, hijo, punto_referencia_inicial,Conjunto_pesos, generacion_0, Conjunto_pesos_vecinos)
# print(act_vecinos)
print(len(act_vecinos))
    
# BUCLE(unimos los pasos anteriores) lo hacemos Generaciones veces:

def bucle(generacion_0, punto_referencia_inicial):
    generacion_resultado = generacion_0
    act_punto_referencia = punto_referencia_inicial
    # it = 0
    for gen_it in range(Generaciones):
        for hijo_it in range(N_poblacion):
            if random.random() > 0.5 :
                # peso_actual_it = Vector_pesos[hijo_it]
                hijo = cruce_DE(hijo_it, Conjunto_pesos, generacion_resultado, Conjunto_pesos_vecinos)
                evaluacion_hijo = funcion_zdt3(hijo)
                act_punto_referencia = actualizar_punto_referencia(act_punto_referencia, evaluacion_hijo)
                generacion_resultado = actualizacion_vecinos(hijo_it, hijo, act_punto_referencia, Conjunto_pesos, generacion_resultado, Conjunto_pesos_vecinos)
    #             it += 1
    # print(it)
    return generacion_resultado

prueba_bucle = bucle(generacion_0, punto_referencia_inicial)
print(test_generacion(prueba_bucle))
p_x = [x[0] for x in prueba_bucle]
p_y = [y[1] for y in prueba_bucle]
plt.scatter(p_x, p_y)



