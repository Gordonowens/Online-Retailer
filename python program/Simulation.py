import datetime
class Simulation():
    """
    this is used to hold non specific data that is used by all classes
    """

    def __init__(self, time, customerFile, orders):

        self.time = time
        self.customers = self.getCustomerData(customerFile)
        self.workers  = self.getWorkerData(workerFilePath)
        self.products = products

    def getCustomerData(self, filepath):
        #read csv

        #create array and set self.custoemrs = to it
        return 1

    def getWorkerData(self, filepath):
        # read csv

        # create array and set self.custoemrs = to it
        return 1



    def getOrder(self):

        if len(self.orders) == 0:
            return []

        else:
            return self.orders.pop()

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