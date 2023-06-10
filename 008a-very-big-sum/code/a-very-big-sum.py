import math
import os
import random
import re
import sys

def aVeryBigSum(ar): #Here the function is defined with an array as its parameter
    aVeryBigSum = 0 #Now we are initalizing the variable to start at 0 and store iterated values
    for i in ar: #Here we are iterating through the array
        aVeryBigSum +=i #Here we add the iterated element to our variable
          
    return aVeryBigSum
                                      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
