from BasicBot import *

class CustomerBot(BasicBot):
    """
    Represent a customer, interacting with online retailer through SQL queries.
    can change it's behavior by modifing frequency and rate variables

    """

    def __init__(self, frequency, database, id, fName, lName, fraudRate,  buyFrequency, defaultRate, generalData, finance = False):
        BasicBot.__init__(self, frequency, database, id, fName, lName, generalData)
        self.order = []
        self.finance = finance
        self.buyFrequency = buyFrequency
        self.fraudRate = fraudRate
        self.defaultRate = defaultRate
        self.id = 500


    def update(self):
        """
        expected to be called from the main function
        uses chance and frequency to determine what actions customer will take
        """

        #check if customer wants to buy
        if self.decision(self.buyFrequency):
            self.buy()


        #check if customer is waiting on any orders
        if (not self.order) != False:
            self.checkOrder()


        #check if customer needs to make a payment, and if customer wants to default
        if self.finance and self.checkPaymentOwing() and self.decision(self.defaultRate):
            #may need to check how default rate works
            self.makeFinancePayment()


    def checkPaymentOwing(self):
        """
        checks if a payment is due or not
        :return: bool
        """
        pass

    def buy(self):
        """
        selects a product based on customer's preference and then sends a SQL to database to place the order
        """

        #select product type
        productType = 0

        #select product
        selectedProduct = self.generalData.getProducts()[productType][1]

        #create query
        print("i buy " + selectedProduct)


        query = "insert into orders (order_id, customer_id, order_date, order_state_id, product_id) values (" + str(self.id) + ", 1," + "'" + str(self.generalData.getTime()) + "'" + ", 1, 3);"

        print(query)

        self.runUpdateQuery(query)

        self.id += 1
        #update customer's orders list


    def checkOrder(self):
        """
        checks the status of customer's order then takes appropriate action based on
        order's status
        """

        #run sql check if order has arrived

        #if cheat run chance to see if should cheat
        pass

    def makeFinancePayment(self):
        """
        send SQL to database updating financing account
        """
        #make payment
        pass



