'''This number takes a number input and doubles it then prints the answer'''
repeating=True 

#Taking the number and printing it

while repeating:
    try:
        number=float(input("please enter a number:"))
        repeating=False
    except ValueError:
        print("Politly you half witted dumbass put in a number or piss off")


print("the answer is " + str(number*2))
