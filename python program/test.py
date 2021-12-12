import mysql.connector
import pandas
import BasicBot
import time

def testFunctions():
  """
  this is a test and returns nothing
  :return:
  """


  return 0


def main():
  """
  this is a function
  :return:
  """
  mydb = mysql.connector.connect(
    host="DESKTOP-S5B5DOL",
    user="gordon",
    password="fjk54#djk^",

    db = "test"
  )

  #print(testFunctions.__doc__)

  #print("Using help:")
  help(testFunctions)

  mycursor = mydb.cursor()


  mycursor.execute("insert into customer (customer_id, customer_name, category_id, customer_phone)\
                   values (1, 'john smith', 5, '04005500');")


  mybot = BasicBot.BasicBot(4, mycursor)

  time.sleep(5)

  mybot.update(8)

if __name__=="__main__":
  main()


