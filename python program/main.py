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

def createCustomers(connection, folderPath):

  customers = []
  # create customers
  customer_header_list = ['fname', 'lname', 'phone', 'fraud', 'buy', 'default']
  customerdf = pd.read_csv(folderPath + 'simulationdata/customers.csv', names=customer_header_list)

  for index, row in customerdf.iterrows():
    # print(row['fname'])

    customers.append(
      CustomerBot(row['fname'], row['lname'], row['phone'], row['fraud'],
                  row['buy'], row['default'], connection))


  return customers


def createWrokers(connection, folderPath):

  workers = []

  # create worker
  worker_header_list = ['position', 'fname', 'lname', 'lazyfreq', 'mistakefreq', 'speed']
  workerdf = pd.read_csv(folderPath + 'simulationdata\workers.csv', names=worker_header_list)

  for index, row in workerdf.iterrows():
    # print(row['fname'])

    workers.append(
      WorkerBot(row['fname'], row['lname'], row['lazyfreq'], row['mistakefreq'],
                row['speed'], row['position'], connection))

  return workers


def createProducts(connection, folderPath):
  product_header_list = ['supplierID', 'description', 'quantity', 'price']
  productdf = pd.read_csv(folderPath + 'simulationdata\products.csv', names=product_header_list)

  for index, row in productdf.iterrows():

    connection.createProduct(row)


def createSuppliers(connection, folderPath):
  supplier_header_list = ['supplierID', 'suppliername', 'supplierphone']
  supplierdf = pd.read_csv(folderPath + 'simulationdata\suppliers.csv', names=supplier_header_list)

  for index, row in supplierdf.iterrows():

    connection.createSupplier(row)

def main():

  """
  this is a function
  :return:
  """
  simulationData = Simulation(datetime.datetime.now())
  folderPath = "C:/Users/User/Documents/online retailer/"
  sqlscriptOne = "C:/Users/User/Documents/online retailer/SQL program/script one.sql"
  sqlScriptTwo = "C:/Users/User/Documents/online retailer/SQL program/script two.sql"

  mydb = mysql.connector.connect(
    host="DESKTOP-S5B5DOL",
    user="gordon",
    password="fjk54#djk^",

    #db = "onlineretailer"
  )

  mydatabase = DataBase(mydb, simulationData)
  try:
    mydatabase.dropDataBase()

  except:
    pass

  #run first script
  mydatabase.runSQLScript(sqlscriptOne)

  #create customers
  customers = createCustomers(mydatabase, folderPath)

  workers = createWrokers(mydatabase, folderPath)

  createSuppliers(mydatabase, folderPath)

  mydatabase.runSQLScript(sqlScriptTwo)

  createProducts(mydatabase, folderPath)

  i = 0
  while i < 2:
    customers[i].born()
    i = i + 1

  i = 0
  while i < 2:
    workers[i].born()
    i = i + 1


  #mydatabase.makeOrder(1, 1)




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


