 
# Creating a class example 
class Biscuit:
    def __init__(self, price, taste, name):
        """
        biscuit details
        """
        self.price = price
        self.taste = taste
        self.name = name

    def printBrand(self):
        """
        printing the details 
        """
        print("Name of the Biscuit is: ", self.name)


b1 = Biscuit(20,"sweet", "Parle")
b2 = Biscuit(25, "cream", "Sunfeast")
b1.printBrand()
b2.printBrand()
 

 