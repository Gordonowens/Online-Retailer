import mysql.connector
import pandas
from CustomerBot import *
from GeneralData import *
import time
import datetime

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
  #help(testFunctions)

  mycursor = mydb.cursor()



  #create general data
  myData = GeneralData(datetime.datetime.now(), [['soccer boots', 'football', 'tennis racket'], ['twighlight', 'harry potter', 'how to look after dog'],
                    ['garden soil', 'bucket', 'shovel']], mydb)

  #create mybot
  mybot = CustomerBot(4, mycursor, 1, 'steve', 'alderman', .1, .5, 0, myData)


  while(myData.getTime().year != 2023):
    #add a day
    myData.addDay()
    #update my bot
    mybot.update()
    #myData.printTime()

  mycursor.execute(
    "select * from orders;")

  myresult = mycursor.fetchall()
  print(myresult)

  mycursor.close()


if __name__=="__main__":
  main()


