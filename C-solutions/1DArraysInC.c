#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    int sum = 0;
    int x;
    
    scanf("%d\n", &n);
    
    int *arr = (int*)malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++){
        scanf("%d\n", &x);
        arr[i] = x;
        sum += x;
    }
    
    printf("%d\n", sum);
    free(arr);
    return 0;
}