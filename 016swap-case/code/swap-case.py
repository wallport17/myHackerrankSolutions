def swap_case(s): #Here the function swap_case is defined with s as the
                  #Parameter
    swapped = s.swapcase() 
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)