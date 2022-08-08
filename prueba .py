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

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item("Phone",100,1)
item1.apply_discount()
print(item1.price)




