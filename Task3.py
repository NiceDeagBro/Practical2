# TASK 2.3
from dataclasses import dataclass, field                        # import of additional modules dataclass and field, from library dataclasses.

@dataclass                                                      # declaring that this class is going to be dataclass
class Item:                                                     # class Item describes three item chracteristics – name, count and price.
    dict = {}                                                   # declaration of the dictionary.
    name: str                                                   # declaration of the name variable.
    count: int = field(default=1)                               # declaration of the count variable.
    price: float = field(default=10.0)                          # declaration of the price variable.
    def get_total_price(self):                                  # method for calculating total price of the item (multiplies count on price).
        return f"Total price: {self.count * self.price}"        # returns a string containing value of the calculation.
    def full_info(self):                                        # method for prinitng all information about the item (name, count, price, total price).
        return f"\nName: {self.name},\nCount: {self.count},\nPrice: {self.price},\nTotal price: {self.get_total_price()}"       # returns a string with full information of the item.
    def to_dict(self):                                          # method for insertation of the values into the dictionary
        self.dict['name'] = self.name                           # key 'name' equals name of the item
        self.dict['count'] = self.count                         # key 'name' count name of the count
        self.dict['price'] = self.price                         # key 'name' price name of the price
        return self.dict                                        # returns keys and its values

@dataclass
class Food(Item):
    def full_info(self):                                        # method for prinitng all information about the item (name, count, price, total price).
        return f"\nFood:\n\tName: {self.name},\n\tCount: {self.count},\n\tPrice: {self.price},\n\tTotal price: {self.get_total_price()}"       # returns a string with full information of the item.


class Drink(Item):
    def full_info(self):                                        # method for prinitng all information about the item (name, count, price, total price).
        return f"Drink:\n\tName: {self.name},\n\tCount: {self.count},\n\tPrice: {self.price},\n\tTotal price: {self.get_total_price()}"       # returns a string with full information of the item.

f1 = Food("Bread", 2, price=0.5)    # creating a variable and assigning values for the first item of class Food()
f2 = Food("Bread", 2, price=0.5)    # creating a variable and assigning values for the second item of class Food()

d1 = Drink("Bread", 2, price=0.5)    # creating a variable and assigning values for the first item of class Drinks()
d2 = Drink("Bread", 2, price=0.5)    # creating a variable and assigning values for the second item of class Drinks()

    
food_list = [f1, f2]            # adding new variables to a list
for f in food_list:                 # for each variable in the list...
    print(f.full_info())            # ...use method full_info()

drink_list = [d1, d2]            # adding new variables to a list
for d in drink_list:                 # for each variable in the list...
    print(d.full_info())            # ...use method full_info()



