# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (2/10)

2.2 - Considere o seguinte experimento: Lançamento de 3 dados simultâneos com 
registro de quantas vezes um determinado resultado pode ser obtido.
    Mostre que a distribuição limite é binomial e que com N tendendo a infinito 
ela converge para um Gaussiana.
    
--------------------------------------
Principais referências:        
    https://docs.scipy.org/doc/scipy/reference/stats.html#continuous-distributions 
    https://www.datacamp.com/community/tutorials/probability-distributions-python
----------------------------------------
Version by Willian Vieira de Oliveira 
26/04/19
Python: 3.7.3
----------------------------------------
"""
# Python Standard Library
import numpy as np
import pylab

def fatorial(n):
    if(n<=1):
        return 1
    else:
        return (n * fatorial(n-1))


def geraProbabilidades(n, p):
    probabilidades = np.zeros(n+1) # Gerado com um espaço a mais, para mander a referencia de 1 a 6
    
    q = 1 - p
    for numP in range(0, n + 1):
        numQ = n - numP
        
        combinacao_n_numP = fatorial(n) / (fatorial(numP) * fatorial(n - numP))
        probabilidades[numP] = combinacao_n_numP * np.power(p, numP) * np.power(q, numQ) # Probabilidade Binomial
    
    return probabilidades


def plot(probabilidades, n):
    bins = np.arange(0, n+1, 1)
    
    # Set a new plot
    pylab.plt.subplots()
    pylab.clf()    
    pylab.plt.bar(bins, probabilidades, color='0.3', ec='0.4', lw=1)
            
    if n <= 10:
        pylab.plt.xticks(np.arange(0, n+1, 1))
    elif n <= 20:
        pylab.plt.xticks(np.arange(0, n+1, 2))
    elif n <= 100:
        pylab.plt.xticks(np.arange(0, n+1, 5))
    else:
        pylab.plt.xticks(np.arange(0, n+1, 20))
    
    pylab.rc('figure', figsize=(8,7))
    pylab.grid(True)
    title = 'Distribuição da probabilidade de ocorrência de um determinado valor \nao se jogar um dado ' + str(n) + ' vezes'
    pylab.plt.title(title)
    pylab.plt.xlabel('Número de sucessos')
    pylab.plt.ylabel('Probabilidade de ocorrência (%)')
    pylab.plt.show()


def menu():
    #n = int(input('Quantos lançamentos de dado? '))
    lances = [3, 10, 100]
    p = 1/6 
    
    for n in lances:
        print("Lançamento de ", n, " dados simultâneos...")
        probabilidades = geraProbabilidades(n, p)
        
        plot(probabilidades, n)
        
        
menu()

"""
    https://www.quora.com/How-many-rolls-does-it-take-for-2-dice-to-generate-a-normal-curve-according-to-probability

The central limit theorem says that the mean of a large amount of random numbers from the same distribution will tend towards being normally distributed.
With two dice you will of course get a sort of "first order approximation" in the form of a triangle. Every throw more you do will make it look a bit more like a normal distribution, although you will never get to the theoretical one which is defined over an infinite domain.
Therefore the only true answer here is "Infinitely many". But throwing them ten times or so will start giving you a distribution which most humans will say looks like a normal distribution.


"""