'''item1= 'phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1)) #str
print(type(item1_price)) # int
print(type(item1_quantity)) # int
print(type(item1_price_total)) # int'''


class Item:
    pay_rate = 0.8 #They pay rate after 20% discount
    def __init__(self, name: str,price:float, quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0,f"Quantity {quantity} is not greater or equal to zero!"

        #Assigm to self object
        self.name = name 
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)

'''print(item1.calculate_total_price())
print(item2.calculate_total_price())'''

'''print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)'''

print(Item.__dict__) #All the attibutes for Class level
print(item1.__dict__) #All the atributes for instance level


'''print(type(item1)) #item
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int'''

'''random_str = "aaa"
print(random_str.upper())'''

