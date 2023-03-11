# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:12:23 2023

@author: fabio
"""
import random

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
    tasa_cruce = 0.5
    individuo_resultado = [0.0]*30
    j = random.randint(0, 29)
    for i in range(30):
        if random.random() <= tasa_cruce or i == j:
            individuo_resultado[i] = individuo_mutante[i]
        else : 
            individuo_resultado[i] = individuo_subproblema[i]
    return individuo_resultado
    

    
    
    
    
    
    
    
    
    
