import math
import os
import random
import re
import sys

def simpleArraySum(ar): #Here we defined the function using the array ar as its parameter. 
    simpleArraySum = 0 #Here we initialize the variable which is used to store the sum
   
   #Here we are iterating through each element in the array. Each element will be added to our variable which
   #will be updated each iteration. 
    for i in ar:
        simpleArraySum = simpleArraySum + i
    return(simpleArraySum) #Here we are returning the value of our sum.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
                                                    
