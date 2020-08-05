""" This submodule implements a class that can manipulate numbers """

class NumManip:
    """This class implements a few different types of methods to manipulate numbers

    Variables:
        class_variable (int): A simple integer

    Attributes:
        num1 (int, float): The first number
        num2 (int, float): The second number 

    Parameters:
        param1 (int, float): The first number given by the user
        param2 (int, float): The second number given by the user

    """
    class_variable = 1

    def __init__(self, param1, param2):
        self.num1 = param1
        self.num2 = param2

    def method(self):
        """This method prints the ratio of 'num1' to 'num2'
        
        """
        print("ratio of {} to {} is {}".format(self.num1, self.num2, self.num1/self.num2))

    @staticmethod
    def another_method(param1, param2):
        """A method used to quickly find the sum of two numbers

        Parameters:
            param1 (float, int): The first number passed by the user
            param2 (float, int): The second number passed by the user

        """
        print("sum is: {}".format(param1+param2))

    @classmethod
    def last_method(cls):
        """A method to quickly find print the class variable

        """
        print("class variable is :{}".format(cls.class_variable))
