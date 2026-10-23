class Inventory:
    items_list = []

    @classmethod
    def add_item(cls, item):
        cls.items_list.append(item)

    @classmethod
    def search_item(cls, item_code):
        for item in cls.items_list:
            if item_code == Item.get_item_code(item):
                return item
        return None


class Item:
    def __init__(self, name, price, quantity, expiry):
        self.__item_code = len(Inventory.items_list) + 1
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__expiry = expiry
        Inventory.add_item(self)

    def show_item(self):
        print(f"Item Code : {self.__item_code}")
        print(f"Name : {self.__name}")
        print(f"Price : {self.__price}")
        print(f"Available : {self.__quantity}pcs")
        print(f"Expiry Date : {self.__expiry}\n")

    def add_stock(self, amount):
        if amount <= 0:
            print("Invalid Amount.\n")
        else:
            self.__quantity += amount
            print(f"After added, new stock for {self.__name} is {self.__quantity}\n")

    def remove_stock(self, amount):
        if amount <= 0:
            print("Invalid Amount.\n")
        elif amount > self.__quantity:
            print("Don't have that much quantity.\n")
        else:
            self.__quantity -= amount
            print(f"After removed, new stock for {self.__name} is {self.__quantity}\n")

    def get_item_code(self):
        return self.__item_code

    def get_item_name(self):
        return self.__name

    def get_item_quantity(self):
        return self.__quantity



def asking_for_item_code():
    try:
        num = int(input("Enter the Item Code: "))
        return num
    except ValueError:
        print("Invalid Code type, Please enter a numeric number.")
        return None


def asking_for_quantity():
    try:
        num = int(input("Enter the quantity: "))
        return num
    except ValueError:
        print("Invalid Code type, Please enter a numeric number.")
        return None


item1 = Item("Milk", 10, 5,"10-12-2026")
item2 = Item("Water", 2, 20,"10-10-2027")
item3 = Item("Butter", 5, 10,"10-12-2026")
item4 = Item("Lipton", 16, 5,"10-12-2027")
item5 = Item("Coffee", 4, 3,"10-5-2028")


while True:
    print("1. View All Items.")
    print("2. Add Stock.")
    print("3. Remove Stock.")
    print("4. Search Item by Item Code.")
    print("5. Low Stock Report.")
    print("6. Exit.\n")

    option = input("Enter option : ")
    if option == "1":
        for item in Inventory.items_list:
            item.show_item()
    elif option == "2":
        item_code = asking_for_item_code()
        if item_code is not None:
            item = Inventory.search_item(item_code)
            if item is not None:
                print(
                    f"{Item.get_item_name(item)}, current stock is {Item.get_item_quantity(item)}."
                )
                quantity = asking_for_quantity()
                if quantity is not None:
                    item.add_stock(quantity)
            else:
                print("Invalid Item Code.")
    elif option == "3":
        item_code = asking_for_item_code()
        if item_code is not None:
            item = Inventory.search_item(item_code)
            if item is not None:
                print(
                    f"{Item.get_item_name(item)}, current stock is {Item.get_item_quantity(item)}."
                )
                quantity = asking_for_quantity()
                if quantity is not None:
                    item.remove_stock(quantity)
            else:
                print("Invalid Item Code.")
    elif option == "4":
        item_code = asking_for_item_code()
        if item_code is not None:
            item = Inventory.search_item(item_code)
            if item is not None:
                item.show_item()
            else:
                print("Invalid Item Code.")
    elif option == "6":
        break
    else:
        print("Invalid Option, Please Select Again.")
