def is_leap(year): #Our defining function
    leap = False
    if (year % 400) == 0 and (year % 100) == 0: #If the year is divisible by
                                                #both 100 and 400
        leap = True #Return True
    elif (year % 100) != 0 and (year % 4) == 0: #If the year is not divisible
                                                #by 100 but is divisible by 4
        leap = True #Return True
                                     
    return leap

year = int(input()) #Here we are asking for user input
print(is_leap(year)) #Here we print either true or false

