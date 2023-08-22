from write import InvoiceGenerator

class Equipment:
    def __init__(self, name, brand, price, qty, *_):
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = qty


class RentalShop:
    def __init__(self, stockFile, statementName = "statement.txt"):
        self.equipments = []
        self.stockFile = stockFile
        self.getStock()
        self.statementName = statementName
        self.InvoiceGen = InvoiceGenerator(self)
        self.fine = 2
    
    def getStock(self):
        file = open(self.stockFile)
        for x in file:
            self.addEquipment(*x.rstrip().split(","))
        file.close()

    def setStock(self):
        file = open(self.stockFile, "w")
        for i in self.equipments:
            file.write(','.join([i.name, i.brand, str(i.price), str(i.stock), ""])+'\n')
        file.close()

    def addEquipment(self, name, brand, price, qty, *_):
        self.equipments.append(Equipment(name, brand, int(price), int(qty)))


    def showEquipments(self):
        print("\nList of Equipments:")
        IdMaxLen    = 4
        priceMaxLen = 6
        nameMaxLen  = 35
        brandMaxLen = 20
        stockMaxLen = 7
        print("Id".center(IdMaxLen) + "Name".center(nameMaxLen) + "Brand".center(brandMaxLen) + "Price".rjust(priceMaxLen) + "Stock".rjust(stockMaxLen))
        for i in range(len(self.equipments)):
            equipment = self.equipments[i]
            print(str(i).center(IdMaxLen) + equipment.name.ljust(nameMaxLen) + equipment.brand.ljust(brandMaxLen) +  ('$'+str(equipment.price)).rjust(priceMaxLen) + str(equipment.stock).rjust(stockMaxLen))
        print("\n")

    def validQty(self, id, qty):
        return self.equipments[id].stock >= qty


    def rentOrder(self, name, orders):
        statementWriter = open(self.statementName, "a")
        # update in statement.txt (add)
        for order in orders.orderList:
            self.equipments[order[0]].stock -= order[1]
            statementWriter.write(','.join([name, *map(str, order)])+'\n')
        self.setStock()
        if orders.orderList:
            self.InvoiceGen.generateOrderInvoice(name, orders)
        statementWriter.close()
        return
    

    def returnOrder(self, name, returnOrders):
        # update in statement.txt (remove)
        orderCopy = []
        for order in returnOrders.orderList:
            orderCopy.append([*order, self.removeStatement(name, order[0])])
        self.setStock()
        if orderCopy:
            self.InvoiceGen.generateReturnInvoice(name, orderCopy)
        return
    

    def removeStatement(self, name, id):    # FIFO logic
        statementReader = open(self.statementName, "r")
        lines = statementReader.readlines()
        firstIndex = -1
        t_qty = 0
        for i, line in enumerate(lines):
            sName, sId, qty, *_ = line.split(",")
            if sName==name and int(sId)==id:
                self.equipments[int(sId)].stock += int(qty)
                firstIndex = i
                t_qty = int(qty)
                break
        if firstIndex==-1: return t_qty
        lines.pop(firstIndex)

        statementReader.close()
        statementReader = open(self.statementName, "w")
        statementReader.writelines(lines)
        statementReader.close()
        return t_qty
