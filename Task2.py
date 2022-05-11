from dataclasses import dataclass, field                        # import of additional modules dataclass and field, from library dataclasses.


@dataclass                                                      # declaring that this class is going to be dataclass
class Item:                                                     # class Item describes three item characteristics – name, count and price.
    dict = {}                                                   # declaration of the dictionary.
    name: str                                                   # declaration of the name variable.
    count: int = field(default=1)                               # declaration of the count variable.
    price: float = field(default=10.0)

    # declaration of the price variable.
    def get_total_price(self):                                  # method for calculating total price of the item (multiplies count on price).
        return f"Total price: {self.count * self.price}"        # returns a string containing value of the calculation.

    def full_info(self):                                        # method for printing all information about the item (name, count, price, total price).
        return f"\nName: {self.name},\nCount: {self.count},\nPrice: {self.price},\nTotal price: {self.get_total_price()}"       # returns a string with full information of the item.

    def to_dict(self):                                          # method for insertion of the values into the dictionary
        self.dict['name'] = self.name                           # key 'name' equals name of the item
        self.dict['count'] = self.count                         # key 'name' count name of the count
        self.dict['price'] = self.price                         # key 'name' price name of the price
        return self.dict                                        # Return keys and its values


i1 = Item("Carrots")                # creating a variable and assigning value for the first item of class Item()
i2 = Item("Milk", 2, 1.5)           # creating a variable and assigning values for the second item of class Item()
i3 = Item("Bread", 2, price=0.5)    # creating a variable and assigning values for the third item of class Item()

item_list = [i1, i2, i3]            # adding new variables to a list
for i in item_list:                 # for each variable in the list...
    print(i.full_info())            # ...use method full_info()
    print(i.to_dict())              # ...use method to_dict()