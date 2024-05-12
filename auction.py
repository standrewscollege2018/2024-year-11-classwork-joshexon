
import sqlite3

DATABASE = "auction.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


def notBlank(userinput):
    if userinput.strip(" ")=="":
        return True
    else:
        return False

def numCheck(number):
    if number.strip(" ")=="":
        return True
    else:
        try:
            number=int(number)
            return False
        except ValueError:
            return True

checkingIntent=True
userIntent=input("do you want to list something(1) or buy something(2): ")
while checkingIntent:
    if userIntent=="1" or userIntent=="2":
        checkingIntent=False
    else:
        userIntent=input("make sure you enter either 1 or 2: ")

if userIntent=="1":
    checkingIName=True
    while checkingIName:
        itemName=input("what are you selling? ")
        checkingIName=notBlank(itemName)
    checkingICat=True
    while checkingICat:
        itemCatagory=input("what catagory is your item in sport(1), technology(2), clothing(3), vehicle(4), other(5): ")
        if itemCatagory=="1" or itemCatagory=="2" or itemCatagory=="3" or itemCatagory=="4" or itemCatagory=="5":
            checkingICat=False
    checkingRPrice=True
    while checkingRPrice:
        reservePrice=input("what is your reserve price $ ")
        checkingRPrice=numCheck(reservePrice)
    checkingSName=True
    while checkingSName:
        sellersName=input("what is your name: ")
        checkingSName=notBlank(sellersName)
    cursor.execute("INSERT INTO item (itemName, itemCatagory, reservePrice, sellersName) VALUES (?,?,?,?)",(itemName, itemCatagory, reservePrice, sellersName))
    connection.commit()
    
    
else:
    buyerName=input("what is your name: ")
    catagotySearch=input("what catagory would you like to search sport(1), technology(2), clothing(3), vehicle(4), other(5): ")
    cursor.execute("SELECT * FROM item WHERE itemCatagory=(?)", (itemCatagory))
    
