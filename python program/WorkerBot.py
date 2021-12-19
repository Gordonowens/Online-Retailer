from BasicBot import *
import random

class WorkerBot(BasicBot):

    def __init__(self, frequency, database, id, fName, lName, generalData, lazyFreq, mistake, speed, lazy = False):


        BasicBot.__init__(self, frequency, database, id, fName, lName, generalData)
        self.lazyFrequency = lazyFreq
        self.mistakeRate = mistake
        self.speed = speed
        self.orders = []


    def update(self):

        #run lazy check if lazy do nothing
        if not self.decision(self.lazyFrequency):

            #if inactive run getorder
            if self.state == 'inactive':
                self.getOrder()
                if len(self.orders) == 0:
                    self.state = 'inactive'

                else:
                    self.state = 'picking'


            #else run pick product
            else:

                # check if any more products to pick
                if len(self.orders) == 0:
                    self.state = 'inactive'

                else:
                    self.pickProduct()

        else:
            print('worker is lazy')

    def getOrder(self):
        #queries database and gets next most relevant order id
        self.orders = self.generalData.getOrder()

        #queries database and updates order

        #queries database and creates new pallet


    def pickProduct(self):

        #run probability for mistake
        #if mistake true update python product variable

        if self.decision(self.mistakeRate):
            print('worker made a mistake')
        else:

            print("worker picks " + self.orders.pop())

        DataBase.pickProduct(x,y,z)

        # check if product available
        #if available update product table

        #update pallet
        #run update order

    def updateOrder(self):

        #query to update product on order table

        #if no more products update order status

        #update worker bot status to inactive

        return 0

