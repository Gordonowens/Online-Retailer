import mysql.connector
from CustomerBot import *
from GeneralData import *
from WorkerBot import *
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
                    ['garden soil', 'bucket', 'shovel']], [['cows milk', 'apples', 'pears'], ['work boots', 'high vis shirt', 'belts']], mydb)

  #create mybot
  mybot = CustomerBot(4, mycursor, 1, 'steve', 'alderman', .1, .1, 0, myData)

  myWorker = WorkerBot(4, mycursor, 1, 'alfred', 'curts', myData, .05, .2, 5)


  while(myData.getTime().year != 2023):

    #add 20 minutes
    myData.addHalfHour()

    #update workerbot
    myWorker.update()

    #add a day
    myData.addDay()
    #update my bot
    #mybot.update()
    #myData.printTime()

  mycursor.execute(
    "select * from orders;")

  myresult = mycursor.fetchall()
  print(myresult)

  mycursor.close()


if __name__=="__main__":
  main()


