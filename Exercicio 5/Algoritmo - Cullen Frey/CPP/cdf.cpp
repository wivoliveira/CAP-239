/* This program computes the data for histogram
   Input the noun of file.dat and vector size N and column */

#include <iostream>
#include<fstream>
#include <stdio.h>
#include <stdlib.h>
#define N  20		// input lenght of file
#define MAX 16.2975	// input column max value
#define MIN 0.0777	// input column min value
#define NB 20		// input number of histogram bins

using namespace std;

int main(){

     double column1[N], column2[N];

     ifstream fData("histgammaR3-15.dat",ios::in);		// INPUT file data name
     if (fData == NULL){
          cout << "File of Data do not exist" << endl;
          exit(1);
     }

//    Npoints = N;

     for (int i=0; i < N; i++)  fData >> column1[i] >> column2[i];

     column2[-1] = 0;
     for (int j=0; j < N; j++)   column2[j] = column2[j] + column2[j-1];

     for (int l=0; l < N; l++)  printf("%5.3f  %6.4f\n", column1[l], column2[l]);


     fData.close();

     return 0;
}
// Itś OK!
