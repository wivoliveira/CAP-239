# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (2/10)

1.3 - Gere o algoritmo em python para somar e normalizar com média zero (<A>=0),
dois sinais com o mesmo tamanho e construa as séries:
    S5 = S1 + S4;
    S6 = S2 + S4;
    S7 = S3 + S4;

    Normalização adotada: Z-Score
        (x_i)' = (x_i - mean(x) ) / std(s), onde:
            
            x_i: valor que se deseja normalizar
            (x_i)': Valor x_i normalizado
            mean(x): Valor média da série x
            std(x): Desvio padrão da série x
            
    Fonte: Abdi (2010)
        https://www.utdallas.edu/~herve/abdi-Normalizing2010-pretty.pdf
        
----------------------------------------
Version by Willian Vieira de Oliveira 
24/04/19
Python: 3.7.3
----------------------------------------
"""

# My code
#import Serie_caotica as Sc

# Python Standard Library
import numpy as np

def normaliza(s):
    s = (s - np.mean(s)) / (np.std(s))
    return s

# load the data previouly generated using the powernoise.m
s1 = np.genfromtxt ('s1.csv', delimiter=",")
s2 = np.genfromtxt ('s2.csv', delimiter=",")
s3 = np.genfromtxt ('s3.csv', delimiter=",")

# Generate the chaotic series
#s4 = Sc.serie_caotica(2**12, 4.0, 0.001)
s4 = np.genfromtxt ('s4.csv', delimiter=",")

# Generate s5, s6, s7:
s5 = s1 + s4
s5 = normaliza(s5)

s6 = s2 + s4
s6 = normaliza(s6)

s7 = s3 + s4
s7 = normaliza(s7)

np.savetxt("s5.csv", s5, delimiter = ",")
np.savetxt("s6.csv", s6, delimiter = ",")
np.savetxt("s7.csv", s7, delimiter = ",")


