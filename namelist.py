keep_going=True
namelist=[]
count=0
while keep_going:
    name=input("enter a name: ")
    if name.lower().strip(" ")=="stop":
        keep_going=False
    else:
        try:
            name=float(name)
            print("enter a name of piss off")
            count=count+1
            if count==3:
                print("you have pissed me off enough you're done")
                keep_going=False
        except ValueError:
            allow=True
            for letters in name:
                try:
                    letter=int(letters)
                    allow=False
                except ValueError:
                    pass
            if allow==True:
                if name.strip(" ")=="":
                    print("enter a name or piss off")
                    count=count+1
                    if count==3:
                        print("you have pissed me off enough you're done")
                        keep_going=False
                else:
                    namelist.append(name)
            else:
                print("stop entering numbers or piss off")
                count=count+1
                if count==3:
                    print("you have pissed me off enough you're done")
                    keep_going=False
                

namelist=sorted(namelist)
for i in range(len(namelist)):
    print(str((i+1)) + ". " + (namelist[i]))
