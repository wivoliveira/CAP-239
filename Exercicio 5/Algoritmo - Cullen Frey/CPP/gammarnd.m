# Script Octave: gera pontos aleatórios da distribuiçaõ gamma
clear all;
clf;
r = 1.5*randg(3,2000,1);
save "pgamma3-15.dat" r;

