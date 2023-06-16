
def split_and_join(line):
    a = line.split(" ") #Here i split line at the spaces and converted it 
                        #into a list of strings
    b = "-".join(a) #Here I declared the variable b which will join the list
                    #of strings with a "-"
    return b #Here I return my 'joined' list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)