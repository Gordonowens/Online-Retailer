import BasicBot
import random

class WorkerBot(BasicBot):

    def __init__(self, frequency, database, id, fName, lName, speed, mistake,  lazy = False):
        BasicBot.__init__(self, frequency, database, id, fName, lName)
        lazy = lazy
        mistakeRate = mistake
        speed = speed


    def update(self):

        #run lazy check if lazy do nothing

        #if inactive run getorder

        #else run pick product

        return 0

    def getOrder(self):
        #queries database and gets next most relevant order id

        #queries database and updates order

        #queries database and creates new pallet
        return 0

    def pickProduct(self):

        #run probability for mistake
        #if mistake true update python product variable

        # check if product available
        #if available update product table

        #update pallet
        #run update order

        return 0

    def updateOrder(self):

        #query to update product on order table

        #if no more products update order status

        #update worker bot status to inactive

        return 0

