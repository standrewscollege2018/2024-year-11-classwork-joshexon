#setting the repeats to true
gettingage=True
gettingweight=True

#asking for age and checking if valid
while gettingage:
    try:
        age = float(input("Please enter your age: "))
        if age > 0:
            gettingage=False
        else:
            print("please enter a positive number")
    except ValueError :
        print("Make sure you enter a number with no letters")
    
#asking for weight and checking if valid
while gettingweight:
    try:
        weight = float(input("please enter your weight: "))
        if weight > 0:
            gettingweight = False
        else:
            print("Make sure you enter a positive number")
    except ValueError :
        print("Make sure you enter a number with no letters")

#checking if user is eligible and printing if they are
if age >= 16  and weight >= 50:
    print("You are eligible")
else:
    print("You are not eligible")
    

