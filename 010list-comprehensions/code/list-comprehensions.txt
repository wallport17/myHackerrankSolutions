if __name__ == '__main__':
    #Here we take input from user and get the integers representing the dimensions of a cubiod
    x = int(input())
    y = int(input())
    z = int(input())
    #Here we are given input that represents the integer the elements of the array can not equal
    n = int(input())
    def get_coordinates(x, y, z):
        #This line will create the coordinates [1, j, k] by iterating i from 0 to x, y, or z. It then takes the sum and checks to see if it the sum is not equal to n. If it isn't it will be added to the list of coordinates.
        coordinates = [[i, j, k] for i  in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
        return coordinates
    print(get_coordinates(x, y, z))
                                                
