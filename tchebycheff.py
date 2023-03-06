# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:12:59 2023

@author: fabio
"""
from zdt3_function import funcion_zdt3

### Formulacion Tchebycheff

# en el algoritmo tenemos que inicializar el punto de referencia
# ver como funciona el vector peso ¿qué peso le paso?

def inicializar_punto_referencia(fitness_poblacion):
    conj_f1 = [fit[0] for fit in fitness_poblacion]
    conj_f2 = [fit[1] for fit in fitness_poblacion]
    return (min(conj_f1),min(conj_f2))
    

def actualizar_punto_referencia(punto_ref_actual, punto_ref_candidato):
    z1_act,z2_act = punto_ref_actual
    z1_can,z2_can = punto_ref_candidato
    
    return (min(z1_act,z1_can),min(z2_act,z2_can))


def tchebycheff(individuo, peso, punto_ref):
    # Esta función devuelve el valor multiobjetivo de la funcion zdt3
    
    tche_1 =  peso[0] * abs(funcion_zdt3(individuo)[0] - punto_ref[0])
    tche_2 =  peso[1] * abs(funcion_zdt3(individuo)[1] - punto_ref[1])
    
    return max(tche_1,tche_2)

################################################################################################################
# PRUEBAS 

# ind = [0.6871328245125292, 0.3881933403372219, 0.0, 0.9866438854917386, 1.0, 0.48600692611160956, 0.13345309163728802, 0.4130006992773175, 0.3475543689316074, 0.0, 0.5420429371139106, 0.43062338311863924, 0.5747511823439526, 0.4608231422660385, 0.054574605748320626, 0.7443736362140543, 0.8087089197590822, 0.3039072314004839, 0.7412149980240239, 0.856659847112298, 0.1632537291495746, 0.7406873835120761, 0.599638954893847, 0.6968527405113449, 0.06562394820830503, 0.1780439788155107, 0.0, 0.06412475735875817, 0.49962868692524137, 0.4955840767594016]
# peso = (0.034482758620689655, 0.9655172413793104)
# punto_ref = (0.035664620314922124, 2.2076025567032755)
# prueba= tchebycheff(ind, peso, punto_ref)
# print(prueba)