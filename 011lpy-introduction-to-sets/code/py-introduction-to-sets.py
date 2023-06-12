def average(array): #Here we define the function average to take array as input
    ray = set(array) #Here we create a set from the input
    average = sum(ray) / len(ray) #Here we calculate average by taking the sum of the set and dividing it by the length
    return average #Here the value of the average is returned to the average() function 


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
