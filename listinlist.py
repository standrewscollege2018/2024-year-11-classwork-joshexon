names=[]
keepgoing=True
temp=[]
count=0
def check(x):
    try:
        x=int(x)
        return True
    except ValueError:
        return False
    
    

while keepgoing:
    temp=[]
    name=input("enter a name: ")
    if name.lower()=="stop":
        keepgoing=False
    else:
       
        if check(name):
            print("enter a name dumbass")
            count=count+1
            if count==3:
                keepgoing=False
        else:
            temp.append(name)
            age=input("enter an age: ")
            if check(age)==False:
                print("enter an age dumbass")
                count=count+1
                if count==3:
                    keepgoing=False
            else:
                temp.append(age)
                names.append(temp)

if count==3:
    print("you have the brain power of matthew bluck so you don't get a list")
else:
    for i in range(len(names)):
        print(f"{i+1}.{names[i][0]} {names[i][1]}")

