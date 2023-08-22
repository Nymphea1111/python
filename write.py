import random
import datetime

# FILE HANDLING

class InvoiceGenerator:
    def __init__(self, shop):
        self.shop = shop

    def getPostfix(self):
        return str(int(random.random()*1000000))
    

    def generateOrderInvoice(self, name, orders):
        invoice = open("rentedInvoice/"+name+"_rent_"+self.getPostfix()+".txt", "w")
        # header
        invoice.write("                                 Natural Event Equipment Rental Shop\n")
        invoice.write("                                         INVOICE\n")
        invoice.write("-------------------------------------------------------------------------------------------\n")
        invoice.write("name: "+ name + "\n")
        invoice.write("date: "+ str(datetime.date.today()) + "\n")
        invoice.write(" ----------------------------------------------------------------------------------------- \n")
        invoice.write("|  id  | Equipment                         | Brand                | Price | Qty |  Total  |\n")
        invoice.write(" ------ ----------------------------------- ---------------------- ------- ----- ---------\n")

        totalPrice = 0
        for order in orders.orderList:
            # order = [id, qty]
            price = self.shop.equipments[order[0]].price
            totalPrice += price * order[1]
            line  = f"|{str(order[0]).center(5)} "
            line += f"| {self.shop.equipments[order[0]].name.ljust(33)} "
            line += f"| {self.shop.equipments[order[0]].brand.ljust(20)} "
            line += f"| {str(price).center(5)} "
            line += f"| {str(order[1]).center(3)} "
            line += f"| {str(price*order[1]).rjust(7)} |\n"
            invoice.write(line)

        invoice.write( " ------ ----------------------------------- ---------------------- ------- ----- ---------\n")
        invoice.write(f"|      |    Grand Total    |                  |       |     | {str(totalPrice).rjust(7)} |\n")
        invoice.write( " -----------------------------------------------------------------------------------------\n")
        invoice.close()



        



    def generateReturnInvoice(self, name, orders):
        invoice = open("returnedInvoice/"+name+"_returned_"+self.getPostfix()+".txt", "w")
        # header
        invoice.write("                                         Natural Event Equipment Rental Shop\n")
        invoice.write("                                                   INVOICE (RETURN)\n")
        invoice.write("------------------------------------------------------------------------------------------------------------------\n")
        invoice.write("name: "+ name + "\n")
        invoice.write("date: "+ str(datetime.date.today()) + "\n")
        invoice.write(" ---------------------------------------------------------------------------------------------------------------- \n")
        invoice.write("|  id  | Equipment                         | Brand                | Price | Qty | Rented Days | Fine   |  Total  |\n")
        invoice.write(" ------ ----------------------------------- ---------------------- ------- ----- ------------- -------- --------- \n")

        totalPrice = 0
        for order in orders:
            # order = [id, rented_days, qty]
            price = self.shop.equipments[order[0]].price
            fine = 0
            if order[1] > 5:
                fine  = self.shop.fine * order[1]
            perEqPrice = price * int(order[2]) + fine
            totalPrice += perEqPrice

            line  = f"|{str(order[0]).center(5)} "                                  # id
            line += f"| {self.shop.equipments[order[0]].name.ljust(33)} "           # name
            line += f"| {self.shop.equipments[order[0]].brand.ljust(20)} "          # brand
            line += f"| {str(price).center(5)} "                                    # price
            line += f"| {str(order[2]).center(3)} "                                 # qty
            line += f"| {str(order[1]).center(11)} "                                # rented days
            line += f"| {str(fine).center(6)} "                                     # fine
            line += f"| {str(perEqPrice).rjust(7)} |\n"                         # total
            invoice.write(line)

        invoice.write( " ------ ----------------------------------- ---------------------- ------- ----- ------------- -------- ---------\n")
        invoice.write(f"|      |    Grand Total                               |                      |       |     |             |        | {str(totalPrice).rjust(7)} |\n")
        invoice.write( " ----------------------------------------------------------------------------------------------------------------\n")
        invoice.close()
