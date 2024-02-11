repeat=True
repeat2=True
def times(a,b):
    return a*b

while repeat:
    try:
        num1=float(input("enter a number: "))
        repeat=False
    except ValueError:
         print("make sure you enter a number")

while repeat2:
    try:
        num2=float(input("enter another number: "))
        repeat2=False
    except ValueError:
         print("make sure you enter a number")

print("The answer is " + str(times(num1,num2)))

