import random

class BasicBot:
    """
    a basic bot has no real functionality
    """

    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
        self.id = 0
        self.state = "inactive"


    def decision(self, probability):
        """
        :param probability: float of probability of returning true
        :return: bool
        """
        return random.random() < probability

    def getName(self):
        return self.fName



