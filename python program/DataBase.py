class DataBase():

    def __init__(self,  connection, simData):

        self.connection = connection
        self.simData = simData

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


    def runSQLScript(self, filePath,):

        with open(filePath, 'r') as sql_file:
            result_iterator = self.connection.cursor().execute(sql_file.read(), multi=True)
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query
                print(f"Affected {res.rowcount} rows")

            self.connection.commit()  # Remember to commit all your changes!

    def createCustomer(self, customer):

        query = "insert into customer (customer_name, customer_phone) values ('" + customer.getName() + "', '" + customer.getPhoneNumber() + "');"

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

    def getCustomersOrders(self, customerID):
        pass


    def createWorker(self, worker):
        query = "insert into warehouseworker (position_id, worker_name, worker_start_date) values (" + str(worker.getPosition()) + ",'" +  worker.getName() + "', '2018-11-01');"

        self.runInsertQuery(query)


    def createBank(self, bank):
        pass

    def createProduct(self, product):

        #print(product['supplierID'])

        query = "insert into product (supplier_id, product_name, product_quantity, product_price) values (" + str(product['supplierID']) + ", '" + str(product['description']) + "', " \
                + str(product['quantity']) + ", " + str(product['price']) + ");"

        self.runInsertQuery(query)

    def createSupplier(self, supplier):

        query = "insert into supplier (supplier_id, supplier_name, supplier_phone) values (" + str(supplier['supplierID']) + ", '" + str(supplier['suppliername']) + "', '" \
                + str(supplier['supplierphone']) + "');"

        self.runInsertQuery(query)

    def getProducts(self):
        pass

    def getOrders(self):
        pass


    def makeOrder(self, orderID, customer_id):

        #new orderstate
        query = "insert into currentstate (state_id, statedate) values (" + str(orderID) +  ",'" + self.simData.getTime().strftime('%Y-%m-%d %H:%M:%S') + "');"
        #print(query)
        self.runInsertQuery(query)

        currentStateId = self.getDataFromDatabase("select current_state_id from currentstate ORDER by current_state_id DESC LIMIT 1;")

        #update order table
        query = "insert into orders (customer_id, current_state_id) values(" + currentStateId + str(customer_id) + ");"
        self.runInsertQuery(query)

        #iterate over products in table

        #new orderstate

        #update orderedproduct table

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

    def getProductsForOrders(self, orderID):
        pass

    def distinctProducts(self):
        pass

    def getCompletedOrder(self, orderId):
        pass
        #sql query that returns pallet for relevant order

    def dropDataBase(self):

        query = "drop database onlineretailer;"
        self.runInsertQuery(query)






