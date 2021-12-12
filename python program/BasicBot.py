import mysql.connector

class BasicBot:
    
    def __init__(self, frequency, database, id, fName, lName):
        self.database = database
        self.frequency = frequency
        fName = fName
        lName = lName
        id = id
        self.state = "inactive"



    def sendQuery(self):
        """
        test one
        :return:
        """

        self.database.execute("select customer.customer_id, customer.customer_name, orders.order_date, product.product_name from customer left join orders on customer.customer_id = orders.customer_id left join product on orders.product_id = product.product_id;")

        myresult = self.database.fetchall()
        print(myresult)

        self.state = "inactive"

    def updateTable(self):
        self.database.execute("insert into orders (order_id, customer_id, order_date, order_state_id, product_id)\
                 values (1, 1, '2018-01-01', 1, 3);")

        self.state = "inactive"



    def runQuery(self, query):

        self.database.execute(query)



    def update(self, time):
        """
        test two
        :param time:
        :return:
        """
        if time % self.frequency == 0:
            self.state = "active"


    def update(self, time):
        self.updateState(time)
        if self.state == "inactive":
            pass

        else:
            self.updateTable()
            self.sendQuery()
        