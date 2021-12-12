import BasicBot
import random

class CustomerBot(BasicBot):

    def __init__(self, frequency, database, id, fName, lName, cheat,  finance = False):
        BasicBot.__init__(self, frequency, database, id, fName, lName)
        finance = finance
        cheat = cheat


    def update(self, time):

        if True:
            self.state = 'buy'


        if True:
            self.state = 'check order'


        if True:
            self.state = "make payment"
        return 0

    def buy(self):

        #select product type

        #select product

        #create query

        query = "insert into orders (order_id, customer_id, order_date, order_state_id, product_id)\
                         values (1, 1, '2018-01-01', 1, 3);"
        self.runQuery(query)


    def checkOrder(self):

        #run sql check if order has arrived

        #if cheat run chance to see if should cheat
        return 0

    def makeFinancePayment(self):

        #check if payments still owing

        #if payments still owing check if broke

        #make payment
        return 0



