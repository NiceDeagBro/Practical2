from dataclasses import dataclass, field


@dataclass
class Item:
    dict = {}
    name: str
    count: int = field(default=1)
    price: float = field(default=10.0)

    def get_total_price(self):
        return f"Total price: {self.count * self.price}"

    def full_info(self):
        return f"\nName: {self.name},\nCount: {self.count},\nPrice: {self.price},\nTotal price: {self.get_total_price()}"

    def to_dict(self):
        self.dict['name'] = self.name
        self.dict['count'] = self.count
        self.dict['price'] = self.price
        return self.dict


@dataclass
class Food(Item):
    def full_info(self):
        return f"\nFood:\n\tName: {self.name},\n\tCount: {self.count},\n\tPrice: {self.price},\n\tTotal price: {self.get_total_price()}"


class Drink(Item):
    def full_info(self):
        return f"Drink:\n\tName: {self.name},\n\tCount: {self.count},\n\tPrice: {self.price},\n\tTotal price: {self.get_total_price()}"


f1 = Food("Bread", 2, price=0.5)
f2 = Food("Bread", 2, price=0.5)

d1 = Drink("Bread", 2, price=0.5)
d2 = Drink("Bread", 2, price=0.5)

    
food_list = [f1, f2]
for f in food_list:
    print(f.full_info())

drink_list = [d1, d2]
for d in drink_list:
    print(d.full_info())
