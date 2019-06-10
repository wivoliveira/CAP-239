### Gnuplot script: plots CDF distribution
set terminal png medium
set output "cdf-GEV.png"
set title 'GEV - Cumulative Distribution Function'
#set ylabel 'counts per bin'
set xlabel 'x'
#set ylabel 'Pobability Density'
set xrange [-1:17]
set yrange [0:1]
#set style fill  solid 0.9 border -1
sigma = 2.2
xi = 0.3
mu = 2.9
isigma = 1/sigma
beta(x) = (x - mu)/sigma
t(x) = 1 + xi*beta(x)
f(x) = 1.04*exp(-t(x)**(-1/xi))
plot 'cdfgammaR3-15.dat' using 1:2 with boxes notitle, \
     f(x) lt 3 lw 2 notitle
unset xlabel
unset ylabel
#

