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

# sql code that we will run to add stuff to the database
sql = ("INSERT INTO users (username, password) VALUES (%s, %s)")

# ask user for data to add to database
usrToSet = input("mi legyen a felhasználónév: ")
pwToSet = input("mi legyen a jelszó: ")

# set up valuse that will be added
val = (usrToSet, pwToSet)

# adding data
mycursor.execute(sql, val)

# commit
mydb.commit()

mycursor.close()
mydb.close()