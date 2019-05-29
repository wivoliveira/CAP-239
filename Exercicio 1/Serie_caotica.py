# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (2/10)

1.2 - Série Caótica a partir do Mapemaneto Quadrático (Logístico) para p = 4.0,
considerando A0 = 0.001.

    Mapeamento logístico (ou Quadrático):
        A_n+1 = p * A_n * (1 - A_n)

----------------------------------------
Version by Willian Vieira de Oliveira 
24/04/19
Python: 3.7.3
----------------------------------------
"""

# Python Standard Library
import numpy as np

def serie_caotica(N, p, A0):
    print("Gerando Série Caótica...")
    
    S = np.zeros(N, dtype=float)  #Array de zeros, de tamanho N
    S[0] = A0
    
    for pos in range(1, N): #A0 foi incluindo como o primeiro valor,
                                # restando o intervalo [1,N), com N-1 valores
        S[pos] = p * S[pos-1] * ( 1 - S[pos-1] )
    
    return S

S4 = serie_caotica(2**12, 4.0, 0.001)
np.savetxt("s4.csv", S4, delimiter = ",")