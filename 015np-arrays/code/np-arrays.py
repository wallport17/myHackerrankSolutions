import numpy #Here we import the NumPy library

def arrays(arr): #Here we define arrays with arr as the parameter
    
    y = numpy.array(arr,float) #Here we created a NumPy array with arr as
                               #input and float as the element type 
    z = y[::-1] #Here we reversed the np array
    return z

arr = input().strip().split(' ')
result = arrays(arr)
print(result)