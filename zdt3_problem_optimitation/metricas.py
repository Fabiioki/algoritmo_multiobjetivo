# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:49:06 2023

@author: Fabio
"""
import numpy as np
import pygmo

from lectura_frente_ideal import Test_nsgaii

# Definir el conjunto de puntos como una matriz numpy
points = np.array([[0.5, 0.2], [0.2, 0.6], [0.8, 0.9]])

# Definir el punto de referencia como un vector numpy
reference_point = np.array([1, 1])

# Crear un objeto de problema de hipervolumen
hv = pygmo.hypervolume(points)

# Calcular el hipervolumen
volume = hv.compute(reference_point)
print("Hipervolumen:", volume)