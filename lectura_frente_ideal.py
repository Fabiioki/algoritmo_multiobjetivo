# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:36:23 2023

@author: fabio
"""
import matplotlib.pyplot as plt
from inicializacion import test_generacion
'''
'''
archivo = open("frente_ideal.txt","r")
lines = archivo.readlines()

lista_f1 = list()
lista_f2 = list()

for line in lines : 
    linea_cortada = line.split()
    f1 = float(linea_cortada[0])
    f2 = float(linea_cortada[1])
    lista_f1.append(f1)
    lista_f2.append(f2)
    
# plt.scatter(lista_f1, lista_f2)
# 
archivo = open("generacion_final_nsgaii.txt","r")
lines = archivo.readlines()
poblacion = list()

for linea in lines:
    linea_cortada= linea.split()
    individuo = [float(elemento) for elemento in linea_cortada[:30]]
    poblacion.append(individuo)
    
# print(poblacion[1])    

# res = True
# for individuo in poblacion:
#     for propiedad in individuo:
#         if propiedad < 0 or propiedad > 1:
#             res = False
#             print(individuo)


test = test_generacion(poblacion)
p_x = [x[0] for x in test]
p_y = [y[1] for y in test]
plt.scatter(p_x, p_y)
# print(poblacion[:2])
pop = poblacion[2:]
p_x1 = [x[0] for x in pop]
p_y1 = [y[1] for y in pop]
plt.scatter(p_x1, p_y1)