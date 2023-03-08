# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:07:11 2023

@author: fabio
"""

import math

def funcion_cf6(x_real):
    def signo(numero):
        res = -1.0
        if numero > 0 :
            res = 1.0
        return res
        
    sum1 = 0 
    sum2 = 0
    yj = 0
    objetivo = tuple()
    restricciones = tuple()
    n_real = x_real
    for j in range(2,n_real):
        if j%2 == 1:
            yj = x_real[j-1] -0.8 *x_real[0]*math.cos(6.0*math.pi*x_real[0] + j*math.pi/n_real )
            sum1 += yj*yj
        
        else:
            yj = x_real[j-1] - 0.8*x_real[0]*math.sin(6.0*math.pi*x_real[0] + j*math.pi/n_real)
            sum2 += yj*yj
        
    objetivo[0] = x_real[0] + sum1
    objetivo[1] = (1.0 - x_real[0]) * (1.0 -x_real[0]) +sum2
    restricciones[0] = x_real[1]-0.8*x_real[0]*math.sin(6.0*x_real[0]*math.pi+2.0*math.pi/n_real) - signo((x_real[0]-0.5)*(1.0-x_real[0]))*math.sqrt(abs((x_real[0]-0.5)*(1.0-x_real[0])))
    restricciones[1] = x_real[3]-0.8*x_real[0]*math.sin(6.0*x_real[0]*math.pi+4.0*math.pi/n_real) - signo(0.25*math.sqrt(1-x_real[0])-0.5*(1.0-x_real[0]))*math.sqrt(abs(0.25*math.sqrt(1-x_real[0])-0.5*(1.0-x_real[0])))
        
    return (objetivo,restricciones)
    