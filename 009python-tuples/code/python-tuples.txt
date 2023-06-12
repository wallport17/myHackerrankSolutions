f __name__ == '__main__':
    n = int(input()) #Here the variable is declared. It asks for an input that will be an intger
    integer_list = map(int, input().split()) #Here we are transforming our input and spliting the string into substrings
                
    t = tuple(integer_list) #Here we are creating a tuple from the integer list
    print(hash(t)) #Here we are printing the hash value of our tuple
                             
