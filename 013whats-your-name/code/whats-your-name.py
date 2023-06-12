
def print_full_name(first, last): #Here the function takes the input first, last
    output = "Hello " + first + " " + last + "! You just delved into python." #Here I created a variable to hold my
                                            #the strings and the input first and last . 
    print(output)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
