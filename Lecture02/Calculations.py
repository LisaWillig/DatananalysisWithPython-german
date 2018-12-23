"""
module to perform simple mathematical calculations
"""

gh
def multiplications(a, b):
    """
    performs multiplication of a and b
    :param a: number
    :param b: number
    :return: a * b
    """

    return a * b


def summation(a, b):
    """
    performs addition of a and b
    :param a: number
    :param b: number
    :return: a * b
    """

    return a + b

class StringOperations():

    def __init__(self, variable):
        self.myClassVar = variable

    def printHello(self):
        print("Hello")

    def printVariable(self, var):
        print(var)

    def printVar(self):
        print(self.myClassVar)