# create a class Fooditem with the below attributes


class Fooditem:
    def __init__(self, iid, name, cat, price):
        self.itemId = iid
        self.itemName = name
        self.itemCategory = cat
        self.itemPrice = price

    def provideDiscount(self,disc):
        if disc> 0:
            self.itemPrice -= (self.itemPrice*disc /100)

# create another calss Restaurant with the below attributes

class Restaurant:
    def __init__ (self,rname,flist):
        self.resName=rname
        self.foodItemsList = flist
    
    def retrieveUpdatedPrice(self,disc,iid):
        for food in self.foodItemsList:
            if ( food.itemId == iid ):
                food.provideDiscount(disc)
                return food 
        return None

if __name__ == "__main__":
    n=int(input())
    foodItemsList=[]
    for i in range (n):
        itemId= int(input())
        itemName=input()
        itemCategory=input()
        itemPrice=int(input())
        foodItemsList.append(Fooditem(itemId,itemName,itemCategory,itemPrice))

    restObj = Restaurant("ashoka",foodItemsList)
    
    itemId = int(input())

    discount= int(input())

    result = restObj.retrieveUpdatedPrice(discount,itemId)

    if result == None:
        print('No food item exists which matches the searched id')
    else:
        print(result.itemName, result.itemPrice,sep= " -")