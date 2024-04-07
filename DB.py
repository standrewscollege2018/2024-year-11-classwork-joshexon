import sqlite3
DATABASE = "car.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("SELECT * FROM car")
results= cursor.fetchall()



print(f"{'ID':5}{'plate':10}{'driver':20}{'make':20}{'model':15}{'year':5} colour")
print("____________________________________________________________________________________")
