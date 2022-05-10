# Create method "get_total_price" inside the class, which  returns item quantity * item price.

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    count: int = field(default=1)
    price: float = field(default=10.0)
    # def __repr__(self):
    #     return f"\nName: {self.name},\nCount: {self.count},\nPrice: {self.price}\n"

    def get_total_price(self):
        return self.count * self.price


i1 = Item("Carrots", 0, 0)
i2 = Item("Milk", 2, 1.5)
i3 = Item("Bread", 2, price=0.5)

print(i3.get_total_price())
