# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (3/10)

3.2 - Considere o exercício anterior e crie um “bootstrap” para gerar 
10 amostras contendo 200 galáxias cada uma. Considere os valores de morfologia
caracterizados pelo parâmetro g1 (da técnica gradiente pattern analysis) dado
na tabela abaixo.
    
                    Irregulares: 1,97 – 1,99
                    Espirais: 1,96 – 1,98
                    Elípticas: 1,92 – 1,96

Aplique o Teorema de Bayes para encontrar a máxima verossimilhança considerando
os modelos Gaussiano.

--------------------------------------
Principais referências:        
    https://www.weirdgeek.com/2018/11/computing-bootstrap-replicate/
----------------------------------------
Version by Willian Vieira de Oliveira 
26/05/19
Python: 3.7.3
----------------------------------------
"""

import numpy as np
import pylab as plt

#---------------------------------Bootstrap------------------------------------

# Definição do mínimo e máximo de cada tipo de região 
#       [Irregulares, Espirais, Elípticas]
tipos = [(1.97, 1.99),(1.96, 1.98),(1.92, 1.96)]
percentuais = [0.165, 0.515, 0.32]

data = [] # Lista para armazenar as 10 amostras com 200 valores
for i in range(0,10):
    x = []
    for p in range(0,3): 
        for i in range(0, int(200*percentuais[p])):
            x.append(round(np.random.uniform(tipos[p][0],tipos[p][1]), 2))
    data.append(x)

np.savetxt("data.csv", np.transpose(data), delimiter = ",")

#------------------------------------------------------------------------------

# Estatísticas 
med = []
std = []
for i in range(0,10):
    med.append(np.mean(data[i]))
    std.append(np.std(data[i]))

results = np.zeros((3, 10, 200))

for i in range(0,3):
    for j in range(0,10):
        for k in range(0,200):
            a = np.power(data[j][k]-med[i], 2)/(2 * np.power(std[i],2))
            results[i,j,k] = 1/(std[i]*np.power(2*np.pi, 1/2)) * np.power(np.e, -a)
           

# EXERCÍCIO INCOMPLETO!

#
#plt.hist(results[0,:,:], bins=4)
#plt.hist(results[0,0,:])

#all_data = np.concatenate(data)

#count_irreg = data[0][np.where(np.logical_and(data[0]>=1.97, data[0]<=1.99))]
#count_espir = data[0][np.where(np.logical_and(data[0]>=1.96, data[0]<=1.98))]
#count_elipt = data[0][np.where(np.logical_and(data[0]>=1.92, data[0]<=1.96))]



#plt.subplots()
#plt.hist(data, bins=4, color='blue', density = True)#, range=[1.97, 1.99])
#plt.subplots()
"""
plt.hist(data[0], bins=4, color='blue', density = True, range=[1.97, 1.99])
plt.subplots()
plt.hist(data[0], bins=4, color='blue', density = True, range=[1.96, 1.98])
plt.subplots()
plt.hist(data[0], bins=4, color='blue', density = True, range=[1.92, 1.96])
"""
#std = np.std(data[0])
#avg = np.mean(data[0])


