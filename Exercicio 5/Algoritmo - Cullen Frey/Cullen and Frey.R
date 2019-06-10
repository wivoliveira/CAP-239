library("fitdistrplus") #Package
library(rio) #Package

#Setting directory of the file
setwd("D:/Estudos/Doutorado - INPE/PRIMEIRO PERÍODO/Matemática Computacional I/Exercícios/Reinaldo/Willian/Exercicio 3/Algoritmo - Cullen Frey/")

#Choosing the file 
f <- import(file = "out.dat")

#trace("descdist",edit=TRUE)

plotdist(f$V10, histo = TRUE, demp = TRUE) #empirical density and cumulative distribuition

descdist(f$V60, boot = 1000) #Cullen and Frey graph

summary statistics

fw <- fitdist(f$V1, "weibull")
fy <- fitdist(f$V1, "gamma")
fw <- fitdist(f$V1, "lnorm")
fw <- fitdist(f$V1, "beta")

summary(fy)

summary(fw)
