
a = int(input("please enter the numerical day of the week: ")) #prompt varable input
print(" ") #space for visual reasons
print ("You entered:") #answer


if a == 0: #setup for nested conditionals using stored variable
    print ("Sunday")
elif a == 1:
    print ("Monday")
elif a == 2:
    print ("Tuesday")
elif a == 3:
    print ("Wednesday")    
elif a == 4:
    print ("Thursday")
elif a == 5:
    print ("Friday")
elif a == 6:
    print ("Saturday")
else:
    print ("Invalid Input")
