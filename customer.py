from datetime import datetime
from write import InvoiceGenerator

class Customer:
    def __init__(self, name, shop):
        self.name = name
        self.day = datetime.now() # customer shop ma aayeko time
        self.shop = shop

        # order objects declaration
        self.orders = Orders()
        self.returnOrders = Orders()


    def printOrders(self):
        for order in self.orders.orderList:
            name = self.shop.equipments[order[0]].name
            brand = self.shop.equipments[order[0]].brand
            price = self.shop.equipments[order[0]].price
            print(f"{order[0]} {name} {brand} {price} {order[1]}")
        print('return orders')
        for order in self.returnOrders.orderList:
            name = self.shop.equipments[order[0]].name
            brand = self.shop.equipments[order[0]].brand
            price = self.shop.equipments[order[0]].price
            print(f"{order[0]} {name} {brand} {price} {order[1]}")


    def rent_equipment(self):
        id = int(input("enter id : "))
        qty = int(input("enter quantity : "))
        #print("id",id,self.shop.equipments)
        if id >= len(self.shop.equipments) or id < 0:
            print("INVALID ID")
            return
        
        #returnTime = int(input("enter return time(days) : "))

        if (self.shop.validQty(id, qty)):
            self.orders.addOrder(id, qty)
        else:
            print("out of stock")


        



    def return_element(self):
        id = int(input("enter id : "))
        days = int(input("enter days : "))
        self.returnOrders.addOrder(id, days)
        # print(f"{id} {name} {brand} {price} {qty}")

    def submit(self):
        self.shop.rentOrder(self.name, self.orders)
        self.shop.returnOrder(self.name, self.returnOrders)



class Orders:
    def __init__(self):
        self.orderList = []

    # qty here is quantity or no of days
    def addOrder(self, id, qty):
        self.orderList.append([id, qty])

    def getQty(self, id):
        for i,j in enumerate(self.orderList):
            if j[0]==id:
                return j[1]
            
