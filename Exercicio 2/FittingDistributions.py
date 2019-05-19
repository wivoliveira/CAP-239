# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (2/10)

2.1 - Escreva um programa em python que, para uma amostra com N resultados, 
ajuste as seguintes PDFs:
    (i) Uniforme
    (ii) Binomial
    (iii) Beta
    (iv) Laplace
    (v) Gamma
    (vi) Expoencial
    (vii) Qui-quadrado
    (viii) Cauchy
    (ix) Gaussiana (Normal)
        
    
-------- EXECUÇÃO DO CÓDIGO-----------

    Para rodar o código com o exemplo já implementado, utilize:
        
        Fit() 
                # Caso os dados não sejam passados por parâmetro, será realizado a 
                # execução de um exemplo utilizando dados de temperatura
                
                # data = pd.Series(sm.datasets.elnino.load_pandas().data.set_index('YEAR').values.ravel())
                # bins = 27
                # Fonte: http://www.statsmodels.org/dev/datasets/generated/elnino.html 
						 https://www.statsmodels.org/devel/release/version0.6.html
                
    Para rodar o código utilizando dados próprios:
        
        Fit(data, bins, distribution)
            # Exemplo:
            # data: array contendo as amostras
                # data = [23.11,24.2,25.37,23.86,23.03,21.57,20.63,20.15,19.67,20.03,20.02,
                    21.8,24.19,25.28,25.6,25.37,24.79,24.69,23.86,22.32,21.44,21.77,22.33,
                    22.89,24.52,26.21,26.37,24.73,23.71,22.34,20.89,20.02,19.63,20.4,20.77,
                    22.39,24.15,26.34,27.36,27.03,25.47,23.49,22.2,21.45,21.25,20.95,21.6,
                    22.44,23.02,25.0,25.33,22.97,21.73,20.77,19.52,19.33,18.95,19.11,20.27,
                    21.3,23.75,24.82,25.14,24.22,22.16,21.2,20.46,19.63,19.24,19.16,19.84,
                    21.19,23.24,24.71,25.9,24.66,23.14,22.04,21.47,20.55,19.89,19.69,20.57,
                    21.58,23.13,26.3,27.63,27.15,26.72,25.04,23.83,22.34,21.8,21.8,22.39,
                    23.69,24.89,26.55,27.09,26.37,24.71,23.23,22.31,20.72,20.62,21.05,21.52,
                    22.5,23.97,25.9,26.94,25.84,24.23,22.57,21.5,20.15,20.23,20.86,21.88,
                    22.55,24.4,25.59,26.01,24.66,23.53,21.83,20.73,20.1,20.56,20.27]
            
            # bins: número de bins
                # bins = 20
            
            # distribution: distribuição a ser considerada
                Opções:
                    beta       : Beta
                    binomial   : Binomial
                    cauchy     : Cauchy
                    chi2       : Qui-Quadrada
                    expon      : Exponencial
                    gamma      : Gamma
                    laplace    : Laplace
                    norm       : Gaussiana (Normal)
                    uniform    : Uniforme
                
            Fit(data=data, bins=20, distribution='norm')
                
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
import scipy.stats
import pylab
import pandas as pd
import statsmodels as sm

def uniforme(_data, x):
    #------ calculando pela equação ------
    #-------------------------------------
    pdf_fitted = np.zeros(np.size(x))
    
    _xmin = _data.min()
    _xmax = _data.max()

    v = 1 / (_xmax - _xmin)
    for i in range(0, np.size(x)):
        pdf_fitted[i] = v
    
    return pdf_fitted

def fatorial(n):
    if(n<=1):
        return 1
    else:
        return (n * fatorial(n-1))

def numInput():
    try:
        number = float(input("Qual a probabilidade de sucesso (p E [0, 1]) a ser adotada na distribuição binomial?  "))
        if(number < 0 or number > 1):
            print("Entre com um valor entre 0 e 1")
            numInput()
    except:
        print("Entre com um valor entre 0 e 1")
        numInput()
    
    return number

def binomial(_data, x, p=None):
    pdf_fitted = np.zeros(np.size(x))
    
    n = np.size(x)    
    
    if (p == None):
        p = numInput()

    
    for k in range(0, n):
        pdf_fitted[k] = ( fatorial(n) / (fatorial(k) * fatorial(n-k)) ) * np.power(p, k) * np.power((1-p),(n-k))
    
    return pdf_fitted, p

def beta(_data, x):
    dist = scipy.stats.beta
    param = dist.fit(_data)
    
    pdf_fitted = dist.pdf(x, *param)
    
    return pdf_fitted

def laplace(_data, x):
    #------ calculando pela equação ------
    #-------------------------------------
    pdf_fitted = np.zeros(np.size(x))
    x2 = np.zeros(np.size(x))
    
    # Scipy package used only to obtain the parameters
    dist = scipy.stats.laplace
    param = dist.fit(_data)
    loc = param[0]
    scale = param[1]   
    
    for i in range(0, np.size(x)):
        x2[i] = (x[i] - loc) / scale
        pdf_fitted[i] = ( (1/2) * ( np.exp(-np.abs(x2[i])) ) ) / scale
    
    return pdf_fitted

def gamma(_data, x):
    #------ usando scipy.stats.gamma ------
    #-------------------------------------
    dist = scipy.stats.gamma
    param = dist.fit(_data)
    
    pdf_fitted = dist.pdf(x, *param)
    
    return pdf_fitted

def exponential(_data, x):   
    #------ usando scipy.stats.expon ------
    #-------------------------------------
    dist = scipy.stats.expon
    param = dist.fit(_data)
    
    pdf_fitted = dist.pdf(x, *param)
    #-------------------------------------
    
    return pdf_fitted

def qui_quadrado(_data, x):
    #------ usando scipy.stats.chi2 ------
    #-------------------------------------
    dist = scipy.stats.chi2
    param = dist.fit(_data)
    
    pdf_fitted = dist.pdf(x, *param)
    return pdf_fitted

def cauchy(_data, x):
    #------ calculando pela equação ------
    #-------------------------------------
    pdf_fitted = np.zeros(np.size(x))
    x2 = np.zeros(np.size(x))
    
    # Scipy package used only to obtain the parameters
    dist = scipy.stats.cauchy
    param = dist.fit(_data)
    loc = param[0]
    scale = param[1]   
    
    for i in range(0, np.size(x)):
        x2[i] = (x[i] - loc) / scale
        pdf_fitted[i] = ( 1/( np.pi * (1 + np.power(x2[i], 2)) ) ) / scale
    
    return pdf_fitted

def gaussian(_data, x):
    #------ calculando pela equação ------
    #-------------------------------------
    pdf_fitted = np.zeros(np.size(x))
    data_mean = np.mean(_data)
    data_std = np.std(_data)#, ddof=1) #Sem usar ddof=1, o resultado é igual ao resultado gerado pelo Matlab
    
    for i in range(0, np.size(x)):
        pdf_fitted[i] = ( 1/(data_std * np.sqrt(2*np.pi)) ) * np.exp( -0.5 * (np.power(x[i]-data_mean, 2)/(np.power(data_std, 2))) )
    
    return pdf_fitted
                        
def plot(_data, bins, name, pdf_fitted, x, ax=None, n_plots = 0, p=None):
    # Set a new plot
    pylab.plt.subplots()
    pylab.clf()
    
    if (ax):
        ax.hist(_data, bins=bins, density=True, color='0.3', ec='1', label='Data' if n_plots==0 else "") 
                                                # color='0.3' represents the gray shade level; 
                                                #ec='1' represents the edge color (1: white)
        ax.plot(x, pdf_fitted, lw=2, label='FDP: '+name)
        n_plots = n_plots + 1
        
    _ = pylab.hist(_data, bins=bins, density=True, color='0.3', ec='1', label='Data' ) 
                                                # color='0.3' represents the gray shade level; 
                                                #ec='1' represents the edge color (1: white)
    pylab.rc('figure', figsize=(8,7))
    if (name == 'Binomial'):
        pylab.title('Histograma com ajuste da FDP ' + name + ' (p = ' + str(p) + ')')
    else:
        pylab.title('Histograma com ajuste da FDP ' + name)
    pylab.xlabel('Dados')
    #pylab.xlabel('Temperatura (C)')
    pylab.ylabel('Frequência')
    pylab.grid(True)
    
    pylab.plot(x, pdf_fitted, lw=3, label='FDP: '+name)
    pylab.legend()
    
    return ax, n_plots

def Fit(data=None, bins=None, distribution=None, p=None):
    
    #if (data == None):
    if (data is None): # Set default example
        #Example data
        data = pd.Series(sm.datasets.elnino.load_pandas().data.set_index('YEAR').values.ravel())
        bins = 27

    if(bins == None): # Set default number of bins
        bins = 25

    # Prepare data and generate the histogram    
    _data = np.array(data)
    y, x = np.histogram(_data, bins=bins, density=True) 
    
    
    if (distribution):
        ax = None
        n_plots = 0
        if distribution == 'norm':
            pdf_fitted = gaussian(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Normal', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'gamma':            
            pdf_fitted = gamma(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Gamma', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'beta':
            pdf_fitted = beta(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Beta', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'cauchy':    
            pdf_fitted = cauchy(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Cauchy', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'chi2':
            pdf_fitted = qui_quadrado(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Qui-Quadrado', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'expon':
            pdf_fitted = exponential(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Exponencial', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'laplace':
            pdf_fitted = laplace(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Laplace', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'uniform':
            pdf_fitted = uniforme(_data, x)
            ax, n_plots = plot(_data=_data, bins=bins, name='Uniforme', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        elif distribution == 'binomial':
            pdf_fitted, p = binomial(_data, x, p) # p is the probability of succes
            ax, n_plots = plot(_data=_data, bins=bins, name='Binomial', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots, p=p)
        else:
            print('Distribuição não encontrada.')
    else:
        # Perform the distribution fitting considering all methods listed in the header
        # Generates all graphs
        fig, ax = pylab.subplots()
        n_plots = 0
        
        pdf_fitted = gaussian(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Normal', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = gamma(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Gamma', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = beta(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Beta', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = cauchy(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Cauchy', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = qui_quadrado(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Qui-Quadrado', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = exponential(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Exponencial', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = laplace(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Laplace', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted = uniforme(_data, x)
        ax, n_plots = plot(_data=_data, bins=bins, name='Uniforme', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots)
        
        pdf_fitted, p = binomial(_data, x, p)#, p=0.25) # p is the probability of succes
        ax, n_plots = plot(_data=_data, bins=bins, name='Binomial', pdf_fitted=pdf_fitted, x=x, ax=ax, n_plots=n_plots, p=p)
    
        # ---- Setting graphic containing all PDFs ----
        ax.set_title('Histograma com ajuste de diferentes PDFs')
        ax.set_xlabel('Dados')
        #ax.set_xlabel('Temperatura (C)')
        ax.set_ylabel('Frequência')
        ax.grid(True)
        ax.legend()

#Fit()
#Fit(distribution='binomial')