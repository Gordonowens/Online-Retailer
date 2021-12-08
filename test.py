import mysql.connector
import pandas
import BasicBot
import time

mydb = mysql.connector.connect(
  host="DESKTOP-S5B5DOL",
  user="gordon",
  password="xxxx",
   
  db = "test"
)


mycursor = mydb.cursor()


mycursor.execute("insert into customer (customer_id, customer_name, category_id, customer_phone)\
                 values (1, 'john smith', 5, '04005500');")


mybot = BasicBot.BasicBot(4, mycursor)

time.sleep(5)

mybot.update(8)


