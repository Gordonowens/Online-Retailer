class DataBase():

    def __init__(self,  connection):

        self.connection = connection

    def getConnection(self):
        """
        :return: database connection
        """
        return self.connection

    def closeConnection(self):
        self.connection.cursor().close()

    def runInsertQuery(self, query):
        self.connection.cursor().execute(query)
        self.connection.commit()


    def createCustomer(self, customer):

        query = "insert into customer (customer_name, customer_phone) values ('" + customer.getName() + "', '" + customer.getPhoneNumber() + "');"

        print(query)


        self.runInsertQuery(query)



    def getDataFromDatabase(self, query):
        """
        sends query to database and returns the results
        should not be used to update database
        :param query: SQL query
        :return: 2d array of data from database
        """

        self.connection.cursor().execute(query)
        self.connection.cursor = self.connection.cursor(buffered=True)
        myresult = self.connection.cursor().fetchall()

        return myresult

    def getCustomers(self):
        query = "select * from customer;"
        return self.getDataFromDatabase(query)



    def createWorker(self, worker):
        query = "insert into warehouseworker (position_id, worker_name, worker_start_date) values (" + str(worker.getPosition()) + ",'" +  worker.getName() + "', '2018-11-01');"



        #print(query)

        self.runInsertQuery(query)


    def createBank(self, bank):
        pass

    def createProduct(self, supplierID, productName, product_quantity, product_price):

        query = "insert into product (supplier_id, product_name, product_quantity, product_price) values (" + str(supplierID) + ", '" + productName + "', " \
                + str(product_quantity) + ", " + str(product_price) + ");"

        print(query)
        self.runInsertQuery(query)

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

        return 1

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
        pass
        #sql query that returns pallet for relevant order

    def dropDataBase(self):

        query = "drop database onlineretailer;"
        self.runInsertQuery(query)

    def runScript(self, filepath):
        query = "source " + filepath
        print(query)
        self.runInsertQuery(query)





