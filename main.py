from operations import RentalShop
from customer import Customer
from write import InvoiceGenerator

#Design
a=("Natural Event Equipment Rental Shop")
print(a.center(130))
b=("Basundhara,Kathmandu")
print(b.center(130))
print ("====================================================================================================================================================")
c=("!Welcome to our Shop !!")
print(c.center(130))
print("")
d=("Hope you find What you are looking for")
print(d.center(130))
print("=====================================================================================================================================================")


print("")
print ("Email us on: natural@gmail.com")
print("")
print ("Contact us : 9860913639")
print("")
print ("Connect with us : Natural Equipment")
print("")
print("______________________________________________________________________________________________________________________________________________________")

shop = RentalShop("stock.txt")
name = ""
while True:
    name = input("enter customer name (0 if none) : ")
    if len(name) == 0:
        print("error, empty customer name\n")
        continue
    elif (name == "0"):
        break
    
        
    customer = Customer(name, shop)
    shop.showEquipments()

    while True:
        
    
        print('type 1 for renting')
        print('type 2 for returning')
        print('type 3 for exiting')
        in_state = int(input(" : "))

        if (in_state==1):
            customer.rent_equipment()     # get input inside
            #InvoiceGenerator.generateOrderInvoice(name,orders)
        elif (in_state==2):
            customer.return_element() # get returning element
        elif (in_state==3):
            customer.submit()
            break
        else:
            print("invalid")

    print("you are exiting")
