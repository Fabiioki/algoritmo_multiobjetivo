# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:12:23 2023

@author: fabio
"""
import random

# Cruce DE : utilizamos 3 individuos elegidos aleatoriamente en la vecindad

# def cruce_DE(vecinos, pesos, generacion):
    
#     def get_padres(pesos_padres,generacion):
#         res = list()
#         for peso in pesos_padres:
#             i = pesos.index(peso)
#             res.append(generacion[i])
#         return res
    
#     def comprobar_individuo(individuo):
#         # comprobar que los valores del individuo sean aptos
        
#         for i in range(len(individuo)):
#             if individuo[i] < 0:
#                 individuo[i] = 0.
#             if individuo[i] > 1:
#                 individuo[i] = 1.
#         return individuo
    
#     padres_pesos = random.sample(vecinos, 3)
#     padres = get_padres(padres_pesos, generacion)

#     padre_1,padre_2,padre_3 = padres
#     temp = [(p2-p3)*0.5 for p2,p3 in zip(padre_2,padre_3)]
#     hijo = [ t+p1 for t,p1 in zip(temp,padre_1) ]
    
#     return comprobar_individuo(hijo)

def cruce_DE(it_individuo, pesos, generacion, pesos_vecinos):
    
    def get_candidatos( pesos, pesos_padres ,generacion):
        res = list()
        for peso_p in pesos_padres:
            indice = pesos.index(peso_p)
            res.append(generacion[indice])
        return res
    
    def comprobar_individuo(individuo):
        # comprobar que los valores del individuo sean aptos
        
        for i in range(len(individuo)):
            if individuo[i] < 0:
                individuo[i] = 0.
            if individuo[i] > 1:
                individuo[i] = 1.
        return individuo    
    
    # peso_indv_actual = pesos[it_individuo]
    pesos_padres = random.sample(pesos_vecinos[list(pesos_vecinos)[it_individuo]] , 3)
    padres = get_candidatos(pesos, pesos_padres, generacion)
    padre_1,padre_2,padre_3 = padres
    temp = [(p2-p3)*0.5 for p2,p3 in zip(padre_2,padre_3)]
    hijo = [ t+p1 for t,p1 in zip(temp,padre_1) ] 
    return comprobar_individuo(hijo)
    # return hijo
    
    

    
    
    
    
    
    
    
    
    
