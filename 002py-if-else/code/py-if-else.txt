#This code follows a number of coditional statements
#to see if the number is 'Weird' or 'Not Weird'
n = int(input().strip()) #Here I am calling for an input from the user
if n % 2 != 0: #Here I'm checking if the number is odd or not
    print("Weird")
else:
    if n >= 2 and n <=5: #Here im checking for a non-odd number
                         #between 2 and 5
        print("Not Weird")
    elif n >= 6 and n <=20: #Here im checking for a non-odd number
                            #between 6 and 20 
        print("Weird")
    elif n > 20: #Here im checking for any non-odd number above 20
        print("Not Weird")
