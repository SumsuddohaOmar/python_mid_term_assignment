class Inventory:
    items_list = []

    @classmethod
    def add_item(cls, item):
        cls.items_list.append(item)


class Item:
    def __init__(self, name, price, quantity):
        self.__item_code = len(Inventory.items_list) + 1
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        Inventory.add_item(self)

    def show_item(self):
        print(f"Item Code : {self.__item_code}")
        print(f"Name : {self.__name}")
        print(f"Price : {self.__price}")
        print(f"Available : {self.__quantity}pcs\n")

    def add_stock(self, amount):
        if amount <= 0:
            print("Invalid Amount.\n")
        else:
            self.__quantity += amount
            print(f'After added, new stock is {self.__quantity}\n')

    def remove_stock(self, amount):
        if amount <= 0:
            print("Invalid Amount.\n")
        elif amount > self.__quantity:
            print("Don't have that much quantity.\n")
        else:
            self.__quantity -= amount
            print(f'After removed, new stock is {self.__quantity}\n')


class PerishableItem(Item):
    pass


item1 = Item("Milk", 10, 5)
item2 = Item("Water", 2, 20)
item3 = Item("Butter", 5, 10)
item4 = Item("Lipton", 16, 5)
item5 = Item("Coffee", 4, 3)

item5.remove_stock(5)
item5.add_stock(-2)
item5.add_stock(10)
item5.remove_stock(13)
item5.show_item()