'''This number takes a number input and doubles it then prints the answer'''
repeating=True 

#Taking the number and printing it
#start a loop for error catching
while repeating:
    try:
        number=float(input("enter a positive number: "))
        if number >= 0:
            repeating=False
        else:
            print("Politly you half witted dumbass put in a positive number or piss off")
    except ValueError:
        print("Politly you half witted dumbass put in a number or piss off")


print(str(number) + " doubled is " + str(number*2))
