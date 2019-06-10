### Gnuplot script: Plots histogram and GEV PDF 
set terminal png medium
set output "pgamma3-15.dat"
set title 'GEV - Gamma Distribution'
#set ylabel 'counts per bin'
set xlabel 'x'
set style fill  solid 0.9 border -1
plot 'histgamma3-15.dat' using 1:2 with boxes notitle
unset xlabel
unset ylabel
# GEV plot
#s = 0.5
#xi = 0.5
#mu = 0
#is = 1/s
#f(x) = is*((1 + xi*((x - mu)/s))**((-1/xi)-1))*exp(-(1 + xi*((xi-mu)/s))**(-1/xi))
#plot f(x)

