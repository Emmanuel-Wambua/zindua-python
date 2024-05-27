class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def get_name(self):
        return self.name
    

class Inventory:
    def __init__(self):
        self.things = []

    def add_item(self,thing):
        self.things.append(thing)

    def remove_item(self):
        naming = input("Please type in the name of item to be removed: ")
        for item in self.things:
            if naming == item.get_name():
                return item.price
            
    def update_item(self):
        old_name = input("Enter old name: ")
        for item in self.things:
            if old_name == item.get_name():
                new_name = input("Enter new name: ")
                self.things.append(new_name)

item1 = Item("Basketball",4,4500)
item2 = Item("Bread",6,300)
item3 = Item("Couch",2,30000)

invention = Inventory()
invention.add_item(item1)
invention.add_item(item2)
invention.add_item(item3)

# print(invention.update_item())

print(invention.things[1].name)

