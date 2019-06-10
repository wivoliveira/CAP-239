/* This program computes the cumulative distribution of data */

#include <iostream>
#include<fstream>
#include <stdio.h>
#include <stdlib.h>
#define RF 0		// 1 relative frequency, otherwise absolute frequency
#define N  1995		// input lenght of file
#define MAX 14.2113	// input column max value
#define MIN 0.0003	// input column min value
#define NB 16		// input number of histogram bins

using namespace std;

int main(){

     int Nbins, nn, y[NB];
     double Vmax, Vmin, step, hist, mstep, column1[N];
     double v1, v2, x[NB];

     ifstream fData("pgamma3-15.dat",ios::in);		// INPUT file data name
     if (fData == NULL){
          cout << "File of Data do not exist" << endl;
          exit(1);
     }

     Nbins = NB;
     if (Nbins < 2) {
  	  cout << "No Histogram, choose Nbins > 2" << endl;
  	  exit(1);
     }
     Vmax = MAX;	
     Vmin = MIN; 
     step = (Vmax - Vmin)/Nbins;
     mstep = step/2.0;
//    Npoints = N;

     for (int i=1; i <= N; i++) {
 	  fData >> column1[i];
     }

     for (int j=0; j<Nbins; j++) {
          v1 = Vmin + j*step;
	  v2 = Vmin + (j+1)*step;
	  nn = 0;
	  for (int k=1; k <= N; k++) {
	       if ((v1 <= column1[k]) && (column1[k] < v2)) { // edit the column for histogram
                     nn = nn + 1;
               }
	  }
	  x[j] = v1 + mstep;
	  if (j == (Nbins-1)) y[Nbins-1] = nn+1;
	  else y[j] = nn;
     }

    for (int l=0; l<Nbins; l++) {
          if (RF == 1) printf("%5.3f  %f\n", x[l], (float) y[l]/N); // Relative frequencies
	  else printf("%5.3f  %d\n", x[l], y[l]);
     }

     fData.close();

     return 0;
}
// Itś OK!
