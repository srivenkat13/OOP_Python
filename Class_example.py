 
# Creating a class example 
class Biscuit:
    def __init__(self, price, taste, name):
        """
        biscuit details
        """
        self.price = price
        self.taste = taste
        self.name = name

    def printBrandDetials(self):
        """
        printing the details 
        """
        print("Name of the Biscuit is: ", self.name)
        print("Taste of the Biscuit is: ", self.taste)
        print("Price of the Biscuit is: ", self.price)


b1 = Biscuit(20,"sweet", "Parle")
b2 = Biscuit(25, "cream", "Sunfeast")
b1.printBrandDetials()
b2.printBrandDetials()
 

 