import mysql.connector, time
from mysql.connector import errorcode

# stuff idk
mydb = None
dbToUse = "zap614733-1"

# function that connects to the mysql database
def connectToDb(dbToConnect: str):
    global mydb 
    mydb = mysql.connector.connect(
        host="mysql-mariadb-25-104.zap-hosting.com",
        user="zap614733-1",
        password="zHCykld3xKxUVRPX",
        database=dbToConnect
    )

# try to connect to the database, if fails then exit
try:
    connectToDb(dbToUse)
except mysql.connector.Error as err:
    print("something went wrong while connecting to mysql database")
    exit(-1)

# connect to database
connectToDb(dbToUse)
mycursor = mydb.cursor()

# askin user if they want to add something to the database or read from it
whatToDo = input("get/add(g/a): ")

if whatToDo == "a":
    # sql code that we will run to add stuff to the database
    sql = ("INSERT INTO test (text, idk) VALUES (%s, %s)")
    
    # ask user for data to add to database
    textToSet = input("mi legyen a text: ")
    idkToSet = int(input("mi legyen az idk: "))
    
    # set up valuse that will be added
    val = (textToSet, idkToSet)
    
    # adding data
    mycursor.execute(sql, val)
    
    # commit
    mydb.commit()
elif whatToDo == "g":
    query = ("SELECT kuksi, text, idk FROM test")
    mycursor.execute(query)
    for (kuksi, text, idk) in mycursor:
        print(kuksi, text, idk)

mycursor.close()
mydb.close()