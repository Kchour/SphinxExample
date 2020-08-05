"""This submodule implements a few classes to manipulate strings """

class Base:
    """A superclass to be inherited by 'ExampleSubmodule21'

    Demonstrates inheritance of class attributes

    Attributes:
        x (str): Hardcoded as "Apple"
        y (str): Hardcoded as "Orange"

    """
    base_variable = "Banana"

    def __init__(self):
        self.x = "Apple"
        self.y = "Orange"

class StrManip(Base):
    """This class inherits 'Base' and is used to do funny things
    
    Variables:
        class_variable (str): A simple string

    Attributes:
        word1 (str): The first word 
        word2 (str): The second word 

    Parameters:
        param1 (str): The first number given by the user
        param2 (str): The second number given by the user

    """
    class_variable = "Hello"

    def __init__(self, param1, param2):
        # initialize the super class
        super().__init__()

        # Set our class attributes
        self.word1 = param1
        self.word2 = param2

    def word_salad(self):
        """This method prints all of the variables together
        
        """
        print("word salad {} {} {} {}".format(self.x, self.y, self.word1, self.word2))
    
    @classmethod
    def class_salad(cls):
        """This method prints all of the class variables together
        
        """
        print("class salad".format(cls.base_variable, cls.class_variable))
