import sqlite3
DATABASE = "epl.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

running=True

while running:
    print("1. average age")
    print("2. goals scored")
    print("3. possession")
    print("4. assists")
    print("5. XG (expected goals)")
    print("6. XG over/under performance")
    print("7. leave")
    search=input("what stat do you want to see? ")

    if search == "1":
        print("1. highest to lowest")
        print("2. lowest to highest")
        order=input("how would you like to sort the teams? ")
        if order == "1":
            cursor.execute("SELECT team,average_age FROM stat ORDER BY average_age DESC")
            results=cursor.fetchall()
            print(f"    {'team name':15} {'average age':11}")
            print(f"{'_'*35}")
            for i in range(len(results)):
                print(f"{i+1:2}. {results[i][0]:15} {results[i][1]:^11}")
