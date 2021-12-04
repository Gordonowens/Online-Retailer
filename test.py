import mysql.connector

mydb = mysql.connector.connect(
  host="DESKTOP-S5B5DOL",
  user="gordon",
  password="xxxxx",
   
  db = "test"
)


mycursor = mydb.cursor()

mycursor.execute("show tables")

myresult = mycursor.fetchall()
print(myresult)

