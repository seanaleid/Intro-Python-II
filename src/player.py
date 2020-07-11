# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f"name: {self.name}, current_room: {self.current_room}"
    
    def drop(self):
        drop_list = []

        if self.inventory:
            for i, val in enumerate(self.inventory):
            # print(list(enumerate(self.inventory)))
                print(i, "=", val)
            drop_item = int(input(f"Type the item number you want to drop :"))
            # print(type(drop_item))
            
            if drop_item <= len(self.inventory) and drop_item >= 0:
                dropped_item = self.inventory.pop(drop_item)
                drop_list.append(dropped_item)
        else:
            print(f"No items in your inventory")
        
        return drop_list

    def get_inventory(self):
        print(self.inventory)