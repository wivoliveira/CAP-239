%{
Matemática Computacional I
Lista de Exercícios (7/10)

7.2 - Obtenha o espectro de singularidade para todos os sinais do exerício 6.

7.3. Com base nos valores obtidos em 7.2, discuta os possíveis processos
subjacentes para cada ST.

--------------------------------------
Principais referências:        
    https://www.frontiersin.org/articles/10.3389/fphys.2012.00141/full
    https://people.engr.ncsu.edu/jwilson/files/mfdfa-pafts.pdf
    
----------------------------------------
Version by Willian Vieira de Oliveira 
26/05/19
Python: 3.7.3
----------------------------------------
%}
%load S3
%load S7
%load S8

scmin=16;
scmax=1024;
scres=19;
exponents=linspace(log2(scmin),log2(scmax),scres);
scale=round(2.^exponents);
q=linspace(-5,5,101);

m=1;

% ------------- S3 -------------
signal3 = S3;
scale = 10:10:length(signal3)/4;
q = -10:1:10;
m = 1;
[Hq3,tq3,alpha3,falpha3,Fq3]=MFDFA1(signal3,scale,q,m,1);
%[Hq,tq,hq,Dq,Fq]

% ----- Psi (manualmente) -----
%{
[hq_min, i_min] = min(alpha3);
Dq_min = falpha3(i_min);
[hq_max, i_max] = max(alpha3);
Dq_max = falpha3(i_max);
[Dq_pico, i_pico] = max(falpha3);
hq_pico = alpha3(i_pico);

Psi3 = (hq_max - hq_min)/hq_pico
%}

% ------------- S7 -------------
signal7 = S7;
scale = 10:10:length(signal7)/4;
q = -10:1:10;
m = 1;
[Hq7,tq7,alpha7,falpha7,Fq7]=MFDFA1(signal7,scale,q,m,1);

% ----- Psi (manualmente) -----
%{
[hq_min, i_min] = min(alpha7);
Dq_min = falpha7(i_min);
[hq_max, i_max] = max(alpha7);
Dq_max = falpha7(i_max);
[Dq_pico, i_pico] = max(falpha7);
hq_pico = alpha7(i_pico);

Psi7 = (hq_max - hq_min)/hq_pico
%}

% ------------- S8 -------------
signal8 = S8;
scale = 10:10:length(signal8)/4;
q = -10:1:10;
m = 1;
[Hq8,tq8,alpha8,falpha8,Fq8]=MFDFA1(signal8,scale,q,m,1);

% ----- Psi (manualmente) -----
%{
[hq_min, i_min] = min(alpha8);
Dq_min = falpha8(i_min);
[hq_max, i_max] = max(alpha8);
Dq_max = falpha8(i_max);
[Dq_pico, i_pico] = max(falpha8);
hq_pico = alpha8(i_pico);

Psi8 = (hq_max - hq_min)/hq_pico
%}
