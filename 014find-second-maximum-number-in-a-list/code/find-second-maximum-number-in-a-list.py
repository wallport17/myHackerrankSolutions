if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
x = list(arr)
x.sort()
max = (max(x))
while max in x:
    x.remove(max)
print(x[-1])
