# create a Class vegetable with below attrbutes

import string

class Vegetable:
    def __init__(self, name, price, quantity):
        self.VegName = name
        self.VegPrice = price
        self.VegQuant = quantity


#  create another Class Store with the below attributes


class Store:
    def __init__(self, sname, vegList):
        self.storeName = sname
        self.vegList = vegList

    def catergorizeVegetablesAlphabetically(self):
        self.vegList.sort(key = lambda x: x.VegName)
        a = list(string.ascii_lowercase)
        alphaVegList={}

        for i in a :
            temp = []
            for j in self.vegList:
                if i == j.VegName[0]:
                    temp.append(j.VegName)
            if len(temp)> 0:
                alphaVegList[i]= tuple(temp)
        
        return alphaVegList

    def filterVegetablesForPriceRange(self,minp, maxp):
        self.vegList.sort(key = lambda x: x.VegName)
        priceVegList=[]

        for i in self.vegList:
            if minp <= i.VegPrice <= maxp:
                priceVegList.append(i.VegName)
        
        return priceVegList


if __name__ == "__main__":
    count=int(input())
    t=[]
    for i in range( count):
        name=input()
        price=float(input())
        quantity=int(input())

        vegobj=Vegetable(name.lower(),price, quantity)
        t.append(vegobj)

    sname = input()
    minp = float(input())
    maxp = float(input())
    storeObj= Store ( sname,t)
    catVegAlpha = storeObj.catergorizeVegetablesAlphabetically()
    priceList = storeObj.filterVegetablesForPriceRange(minp,maxp)

    for keys, values in catVegAlpha.items():
        print(keys)
        for x in values:
            print(x)
    
    print(str(minp)+'-'+str(maxp))
    if len(priceList) > 0:
        for x in priceList:
            print(x)
    else:
        print(" No vegetable in the give price range ")