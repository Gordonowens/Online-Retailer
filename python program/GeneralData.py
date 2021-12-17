import datetime
class GeneralData():
    """
    this is used to hold non specific data that is used by all classes
    """

    def __init__(self, time, products, orders, connection):

        self.time = time
        self.products = products
        self.orders = orders
        self.connection = connection

    def getOrder(self):

        if len(self.orders) == 0:
            return []

        else:
            return self.orders.pop()




    def getConnection(self):
        """
        :return: database connection
        """
        return self.connection

    def updateProducts(self, index, newProducts):
        """
        :param index: int
        :param newProducts: list of strings
        """
        self.products[index] = newProducts

    def getProducts(self):
        """
        returns the products customer can buy
        :return: list of strings
        """
        return self.products

    def addDay(self):
        """adds day to time"""
        self.time += datetime.timedelta(days=1)

    def addMonth(self):
        """
        adds month to time
        """
        self.time += datetime.timedelta(month=1)


    def addHalfHour(self):
        """
        adds half hour
        """

        self.time += datetime.timedelta(minutes=30)

    def getTime(self):
        """
        :return: datetime
        """
        return self.time

    def printTime(self):
        print(self.time)