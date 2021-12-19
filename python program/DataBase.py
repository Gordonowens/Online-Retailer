class DataBase():

    def __init__(self,  connection):

        self.connection = connection

    def getConnection(self):
        """
        :return: database connection
        """
        return self.connection


    def createCustomer(self, customer):
        pass

    def createWorker(self, customer):
        pass

    def createBank(self, bank):
        pass

    def createProduct(self, product):
        pass

    def getProducts(self):
        pass

    def getOrders(self):
        pass

    def getPallets(self, orderId):
        pass

    def makeOrder(self, order):

        #new orderstate

        #update order table

        #iterate over products in table

        #new orderstate

        #update orderedproduct table

        return orderID

        pass

    def newCurrentState(self, objectId, stateId):
        #insert new state into currentstate table

        #get currentstate_id

        #return currentstate_id
        pass



    def assignWorker(self, orderId):
        #insert new pallet state into current state

        #create new pallet

        #update worker pallet ID
        pass

    def pickProduct(self, productId):
        #create new state for orderedproduct

        #insert relevent row into pallet
        pass


    def getCompletedOrder(self, orderId):
        #sql query that returns pallet for relevant order




