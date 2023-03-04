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
    
def actualizar_punto_referencia(fitness_poblacion, punto_referencia):
    z1,z2 = punto_referencia
    z1_candidato = min([fit[0] for fit in fitness_poblacion])
    z2_candidato = min([fit[1] for fit in fitness_poblacion])
    
    if z1_candidato < z1:
        z1 = z1_candidato
    if z2_candidato < z2:
        z2 = z2_candidato
        
    return(z1,z2)
    

def tchebycheff(individuo, vector_peso, punto_ref):
    # Esta función devuelve el valor multiobjetivo de la funcion zdt3
    
    tche_1 =  vector_peso[0] * abs(funcion_zdt3(individuo) - punto_ref[0])
    tche_2 =  vector_peso[1] * abs(funcion_zdt3(individuo) - punto_ref[1])
    
    return min(tche_1,tche_2)