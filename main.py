import math
import random
import matplotlib.pyplot as plt
import numpy as np

from pesos import crear_pesos, vecindad_pesos
from tchebycheff import tchebycheff, inicializar_punto_referencia, actualizar_punto_referencia
from zdt3_function import funcion_zdt3


# Parámetros de entrada establecidos:
    # N_poblacion: tamaño de la población
    # Generaciones: Número de generaciones
    # T_vecindad : Tamaño de vecindad
N_poblacion = 40
Generaciones = 250
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
Vector_pesos = crear_pesos(N_poblacion)

# Conjunto B(i) para cada vector peso calculamos sus T vectores vecinos 
Conjunto_pesos_vecinos = vecindad_pesos(Vector_pesos, T_vecindad)
print(type(Conjunto_pesos_vecinos))
# Inicializamos la población incial
def generacion_inicial(n_indivuos):
    # Crea tantos individuos como el parámetro que pasemos
    ls_individuos = list()
    
    for _ in range(n_indivuos):
        ls_individuos.append([random.random() for _ in range(30)])
        
    return ls_individuos

generacion_0 = generacion_inicial(N_poblacion)
# print(generacion_0)
# Evaluamos las prestaciones de la generación inicial
def test_generacion(individuos):
    puntos = list()
    for individuo in individuos:
        puntos.append(funcion_zdt3(individuo))
    return puntos

evaluacion_generacion_0 = test_generacion(generacion_0)

# print("generacion 0",evaluacion_generacion_0)
# p_x = [x[0] for x in evaluacion_generacion_0]
# p_y = [y[1] for y in evaluacion_generacion_0]
# plt.scatter(p_x, p_y)

# Inicializamos los puntos de referencia (z1,z2):
z1_inicial, z2_inicial = inicializar_punto_referencia(evaluacion_generacion_0) # ponemos 100 para poder inicializar los puntos de referencia
#print(z1_inicial,z2_inicial)

# Unir individuos con sus pesos
# lambda_individuos = list(zip(vector_pesos, generacion_0))
# print("vector pesos",lambda_individuos)




##############################################################################################################
# ITERACIONES
# Reproducción: Selecciona aleatoriamente índices de B(i) y genera una nueva solución "y" usando operadores evolutivos. (y = es hijo)
# Cruce DE : utilizamos 3 individuos elegidos aleatoriamente en la vecindad

def cruce_DE(vecinos, pesos, generacion):
    
    def get_padres(pesos_padres,generacion):
        res = list()
        for peso in pesos_padres:
            i = pesos.index(peso)
            res.append(generacion[i])
        return res
    
    def comprobar_individuo(individuo):
        # comprobar que los valores del individuo sean aptos
        
        for i in range(len(individuo)):
            if individuo[i] < 0:
                individuo[i] = 0.
            if individuo[i] > 1:
                individuo[i] = 1.
        return individuo
    
    padres_pesos = random.sample(vecinos, 3)
    padres = get_padres(padres_pesos, generacion)

    padre_1,padre_2,padre_3 = padres
    temp = [(p2-p3)*0.5 for p2,p3 in zip(padre_2,padre_3)]
    hijo = [ t+p1 for t,p1 in zip(temp,padre_1) ]
    
    return comprobar_individuo(hijo)


# peso_e, individuo_e = lambda_individuos[0]
# print("ejemplo : ", ex)

vecinos_prueba = Conjunto_pesos_vecinos[(0.0, 1.0)] #vecinos
hijo = cruce_DE(vecinos_prueba, Vector_pesos, generacion_0)
# print("Hijo: ", hijo)


# Evaluación: Evaluar F(y)
evaluacion_hijo = funcion_zdt3(hijo)
# print(evaluacion_hijo)

# Actualización del punto de referencia
act_punto_referencia = actualizar_punto_referencia((z1_inicial, z2_inicial), evaluacion_hijo)
# print(act_punto_referencia)



# Actualización de vecinos
def actualizacion_vecinos(peso, hijo, generacion ,punto_referencia):
    def get_individuos_vecinos(pesos_vecinos,generacion):
        res = list()
        for peso in pesos_vecinos:
            i = Vector_pesos.index(peso)
            res.append(generacion[i])
        return res
    
    pesos_vecinos = Conjunto_pesos_vecinos[peso]
    individuos_vecinos = get_individuos_vecinos(pesos_vecinos, generacion)
    gte_hijo = tchebycheff(hijo, peso, punto_referencia)
    for i in range(len(pesos_vecinos)):
        gte_vecino = tchebycheff(individuos_vecinos[i],pesos_vecinos[i],punto_referencia)
        if gte_hijo <= gte_vecino:
            puesto = Vector_pesos.index(pesos_vecinos[i])
            generacion[puesto] = hijo
            print("ha cambiadoooooooooooooooooooooooooooooooooooooooooo")
    return generacion
    
act_vecinos = actualizacion_vecinos((0.15384615384615385, 0.8461538461538461), hijo, generacion_0, act_punto_referencia)
print(len(act_vecinos))
    
# BUCLE(unimos los pasos anteriores) lo hacemos Generaciones veces:

def bucle(generacion_0, punto_referencia_inicial):
    generacion_resultado = generacion_0
    it = 0
    for gen_it in range(Generaciones):
        for hijo_it in range(N_poblacion):
            if random.random() > 0.5 :
                peso_actual_it = Vector_pesos[hijo_it]
                print("olaaaaaaaaaaaaaaa",peso_actual_it)
                hijo = cruce_DE(Conjunto_pesos_vecinos[peso_actual_it], Vector_pesos,generacion_resultado)
                evaluacion_hijo = funcion_zdt3(hijo)
                act_punto_referencia = actualizar_punto_referencia(punto_referencia_inicial, evaluacion_hijo)
                generacion_resultado = actualizacion_vecinos(peso_actual_it,hijo,generacion_resultado,act_punto_referencia)
                it += 1
            
    print(it)
    return generacion_resultado

prueba_bucle = bucle(generacion_0,(z1_inicial, z2_inicial))
print(test_generacion(prueba_bucle))
p_x = [x[0] for x in prueba_bucle]
p_y = [y[1] for y in prueba_bucle]
plt.scatter(p_x, p_y)



