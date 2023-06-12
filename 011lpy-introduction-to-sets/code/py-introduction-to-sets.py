def average(array):
    ray = set(array)
    average = sum(ray) / len(ray)
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
