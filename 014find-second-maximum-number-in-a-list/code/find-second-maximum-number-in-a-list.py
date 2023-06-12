if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
x = list(arr) #Here I create a list from arr
x.sort() #Here I sort that list from smallest to largest
max = (max(x)) #Here a create a variable to hold the max value of the list
while max in x: #Here I create a check that removes all value equal to the max
    x.remove(max)
print(x[-1])
