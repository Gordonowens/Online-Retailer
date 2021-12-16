import random

class BasicBot:
    """
    a basic bot has no real functionality
    """
    def __init__(self, frequency, database, id, fName, lName, generalData):
        self.database = database
        self.frequency = frequency
        self.fName = fName
        self.lName = lName
        self.id = id
        self.state = "inactive"
        self.generalData = generalData

    def decision(self, probability):
        """
        :param probability: float of probability of returning true
        :return: bool
        """
        return random.random() < probability

    def getDataFromDatabase(self, query):
        """
        sends query to database and returns the results
        should not be used to update database

        :param query: SQL query
        :return: 2d array of data from database
        """

        self.database.execute("select customer.customer_id, customer.customer_name, orders.order_date, product.product_name from customer left join orders on customer.customer_id = orders.customer_id left join product on orders.product_id = product.product_id;")

        myresult = self.database.fetchall()

        return myresult

    def runUpdateQuery(self, query):
        """
        sends query to database to update table
        :param query:
        """

        self.generalData.getConnection().cursor().execute(query)
        self.generalData.getConnection().commit()
