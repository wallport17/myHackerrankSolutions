import math
import os
import random
import re
import sys

def simpleArraySum(ar): #Here we defined the function using the array ar as its parameter. 
    simpleArraySum = 0 #Here we initialize the variable which is used to store the sum
    for i in ar:
        simpleArraySum = simpleArraySum + i
    return(simpleArraySum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
                                                    
