# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:36:23 2023

@author: fabio
"""
import matplotlib.pyplot as plt

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
    
plt.scatter(lista_f1, lista_f2)