def swap_case(s): #Here the function swap_case is defined with s as the
                  #Parameter
    swapped = s.swapcase() #Here the variable swapped is declared.
                           #.swapcase is a method that switches 
                           # uppercase w/ lowercase and calls on s 
    return swapped #Now swapped is returned to the defined function 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)