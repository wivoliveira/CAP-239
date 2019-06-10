library("fitdistrplus") #Package
library(rio) #Packaeg

#Setting directory of the file
#setwd("D:/Estudos/Doutorado - INPE/PRIMEIRO PERÍODO/Matemática Computacional I/Exercícios/Reinaldo/Willian/Exercicio 5/")

#Select the data
f <- read.csv(file="data.csv", header=FALSE, sep=",")
#f <- read.csv(file="data_2000.csv", header=FALSE, sep=",")

#trace("descdist",edit=TRUE)

#sample <- f$V1 # Define which sample is going to be analysed
sample <- f$V1
plotdist(sample, histo = TRUE, demp = TRUE) #empirical density and cumulative distribuition

descdist(sample, boot = 1000) #Cullen and Frey graph

#summary statistics
#fw <- fitdist(sample, "weibull")
#fy <- fitdist(sample, "gamma")
#fw <- fitdist(sample, "lnorm")
#fw <- fitdist(sample, "beta")
#
#summary(fy)
#
#summary(fw)
