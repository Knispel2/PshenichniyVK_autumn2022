#include <stdio.h>
#include <stdlib.h>

int multMatrixSqBad(float *a,  float *b, float *c, int n){
	int i, j, k;
	for (i=0; i<n; i++){
		for (j=0; j<n; j++){
			c[i*n+j]=0;
			for (k=0; k<n; k++){
				c[i*n+j]+=a[i*n+k]*b[k*n+j];
			}
		}
	}
	return 0;
}