'''setting the repeats to true'''
repeat=True



#asking for age and checking if valid
def check(a):
    try:
        a=float(a)
        if a>=0:
            return False
        else:
            return True
    
    except ValueError:
        return True
        


while repeat:
    age= (input("enter your age: "))
    repeat = check(age)
    if repeat==True:
        print("Make sure you enter a positive number")
age=float(age)
if age<16:
    print("You are not eligible")
else:
    repeat=True
    while repeat:
        weight=(input("enter you weight: "))
        repeat=check(weight)

    weight=float(weight)
    if weight<50:
        print("You are not eligible")
    else:
        print("You are eligible")



    


