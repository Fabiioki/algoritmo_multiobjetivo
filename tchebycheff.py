# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:12:59 2023

@author: fabio
"""
import math

from zdt3_function import funcion_zdt3

#------------------------------------------------------------------------------------------------------------------------------
# Función tchebycheff

def tchebycheff(individuo, peso, punto_ref):
    # Esta función devuelve el valor multiobjetivo de la funcion zdt3
    
    tche_1 =  peso[0] * abs(funcion_zdt3(individuo)[0] - punto_ref[0])
    tche_2 =  peso[1] * abs(funcion_zdt3(individuo)[1] - punto_ref[1])
    
    return max(tche_1,tche_2)


#------------------------------------------------------------------------------------------------------------------------------
# Pesos

def crear_pesos(N_pob):
    return  [(i/(N_pob-1), 1-i/(N_pob-1)) for i in range(N_pob)]




def distancia_vecinos(vector, vectores):
    def dist_euc (v1, v2):
        v1x,v1y = v1
        v2x,v2y = v2
        return math.sqrt((v2x-v1x)**2 + (v2y-v1y)**2)
    # Dado un vector peso devuelve todas las distancias que tiene con los demas vectores peso 
    ls_out = list()
    for it in range(len(vectores)):
        ls_out.append((it, dist_euc(vector,vectores[it])))
    return ls_out

def vecindad_pesos(v_pesos,vecindad): # Devuelve los INDICES de los vecinos
    # Devuelve los vecinos más cercanos de un vector peso dado un porcentaje de vecinos que queremos
    # Clave = (vector_peso, puesto) : Valor = Conjunto de pesos vecinos
    vecinos = dict()
    n_vec = math.floor(vecindad*len(v_pesos))
    # it = 0
    for vector in v_pesos:
        aux = distancia_vecinos(vector,v_pesos)
        aux.sort(key = lambda x : x[1])
        vecinos_vector = aux[:n_vec]
        # vecinos[(vector,it)] = [v[0] for v in vecinos_vector]
        vecinos[(vector)] = [v[0] for v in vecinos_vector]
        # it += 1
    return vecinos


#------------------------------------------------------------------------------------------------------------------------------
# Puntos de referencia

def inicializar_punto_referencia(fitness_poblacion):
    conj_f1 = [fit[0] for fit in fitness_poblacion]
    conj_f2 = [fit[1] for fit in fitness_poblacion]
    return (min(conj_f1),min(conj_f2))
    

def actualizar_punto_referencia(punto_ref_actual, punto_ref_candidato):
    z1_act,z2_act = punto_ref_actual
    z1_can,z2_can = punto_ref_candidato
    
    return (min(z1_act,z1_can),min(z2_act,z2_can))


################################################################################################################################################################################################################################
# PRUEBAS 

# ind = [0.6871328245125292, 0.3881933403372219, 0.0, 0.9866438854917386, 1.0, 0.48600692611160956, 0.13345309163728802, 0.4130006992773175, 0.3475543689316074, 0.0, 0.5420429371139106, 0.43062338311863924, 0.5747511823439526, 0.4608231422660385, 0.054574605748320626, 0.7443736362140543, 0.8087089197590822, 0.3039072314004839, 0.7412149980240239, 0.856659847112298, 0.1632537291495746, 0.7406873835120761, 0.599638954893847, 0.6968527405113449, 0.06562394820830503, 0.1780439788155107, 0.0, 0.06412475735875817, 0.49962868692524137, 0.4955840767594016]
# peso = (0.034482758620689655, 0.9655172413793104)
# punto_ref = (0.035664620314922124, 2.2076025567032755)
# prueba= tchebycheff(ind, peso, punto_ref)
# print(prueba)


################################################################################################################
# PRUEBAS 

# N = 30
# vectores_peso =  [(i/(N-1), 1-i/(N-1)) for i in range(N)]
# print(vectores_peso)
# print(distancia_vecinos(vectores_peso[0], vectores_peso))
# vecindad = 0.20
# vecinos = vecindad_pesos(vectores_peso, vecindad)[(1.0, 0.0)]

# print(vecinos)
# print(random.sample(vecinos, 3))

################################################################################################################
