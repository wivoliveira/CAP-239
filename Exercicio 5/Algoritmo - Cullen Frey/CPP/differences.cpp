/* This program computes the differences between data */

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <cmath>
#define N 2000		// input number

using namespace std;

int main(){

    int i, j;
    double diff[N], col1[N];
    char fn[20]="diff5pgamma3-15.dat";
    FILE *fw;

    ifstream fData1("pgamma3-15.dat",ios::in);	// input Datafile name
    fw = fopen(fn, "w+");

    int Nlines = N;
    for (int j=1; j<=Nlines; j++) {
	 fData1 >> col1[j];
    }

    for (int i=1; i<=Nlines-5; i++) {
         diff[i] = col1[i] - col1[i+5];
         diff[i] = fabs(diff[i]);		// fabs(double) is double
         fprintf(fw, "%9.7f\n", diff[i]);
    }

    fclose (fw);
    fData1.close();

    return 0;
}

