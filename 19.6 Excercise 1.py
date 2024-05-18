
def readposint(): #create function
    try:
        num = int(input("Enter a positive integer: ")) #prompts for a positive integer and forces a coversion into integer if a non integer number is entered
    
        if num > 0:
            print(str(num) + " is a positive integer, good job") #rewards correct inputs
    
        else:
            print('That is not a positive integer, try again') #handles negatives
            
    except ValueError:
        print('That is not a positive integer bro, try again') #handles letters, symbols, and other crap
        

readposint() #calls function
