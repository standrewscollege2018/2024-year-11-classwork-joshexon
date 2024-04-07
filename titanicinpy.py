import sqlite3
DATABASE = "titanic.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


checking_clas=True
while checking_clas:
    clas=input("what class would you like to search(1-3)?")
    try:
        clas=int(clas)
        if clas==1 or clas==2 or clas==3:
            checking_clas=False
        else:
            print("your number must be 1, 2 or 3")
    except ValueError:
        print("your answer must be a number")

checking_survived=True
while checking_survived:
    survived=input("would you like to see who survived(1) or who didn't(0)?")
    try:
        survived=int(survived)
        if survived==1 or survived==0:
            checking_survived=False
        else:
            ("make sure you only enter 1 or 0")
    except ValueError:
        print("your answer must be a number")
    




cursor.execute("SELECT * FROM titanic WHERE class=? AND survived=?", (clas, survived))
results= cursor.fetchall()

print(results)





























              
