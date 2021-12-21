import mysql.connector
from CustomerBot import *
from Simulation import *
from WorkerBot import *
from DataBase import *
import datetime

import pandas as pd



def testFunctions():
  """
  this is a test and returns nothing
  :return:
  """


  return 0


def setUpDataBase(database, customers, workers, productdf):

  #drop database
  database.dropDataBase()

  #set up database
  database.runScript("C:\\Users\\User\\Documents\\online retailer\\online retailer.sql")

  #set up customers
  for i in customers:
    i.born()

  #set up workers
  for i in workers:
    i.born()

  #set up products
  for index, row in productdf.iterrows():
    database.createProduct(row['supplierID'], row['description'], row['quantity'], row['price'])

def main():

  """
  this is a function
  :return:
  """


  mydb = mysql.connector.connect(
    host="DESKTOP-S5B5DOL",
    user="gordon",
    password="fjk54#djk^",

    db = "onlineretailer"
  )

  mydatabase = DataBase(mydb)

  customers = []
  workers = []

  #create customers
  customer_header_list = ['fname', 'lname', 'phone', 'fraud', 'buy', 'default']
  customerdf = pd.read_csv('simulationdata\customers.csv', names=customer_header_list)

  for index, row in customerdf.iterrows():
    # print(row['fname'])

    customers.append(
      CustomerBot(row['fname'], row['lname'], row['phone'], row['fraud'],
                row['buy'], row['default'], mydatabase))

  # create worker
  worker_header_list = ['position', 'fname', 'lname', 'lazyfreq', 'mistakefreq', 'speed']
  workerdf = pd.read_csv('simulationdata\workers.csv', names=worker_header_list)

  for index, row in workerdf.iterrows():
    # print(row['fname'])

    workers.append(
      WorkerBot(row['fname'], row['lname'], row['lazyfreq'], row['mistakefreq'],
                row['speed'], row['position'], mydatabase))

  product_header_list = ['supplierID', 'description', 'quantity', 'price']
  productdf = pd.read_csv('simulationdata\products.csv', names=product_header_list)

  setUpDataBase(mydatabase, customers, workers, productdf)

'''
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
  print(type(myresult))
'''





if __name__=="__main__":
  main()


