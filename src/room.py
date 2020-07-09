# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomID, name, description, items):
        self.roomID = roomID
        self.name = name
        self.description = description
        self.items = []

    def look(self):
        foundItems = []

        for item in self.items:
            itemName = item[0]
            print(f"You found {itemName}")
            choice = input(f"Do you want to take it? y/n ")

            if choice == 'y':
                print(f"{itemName} added to your inventory")
                self.items.pop(itemName)
                foundItems = itemName
            
            elif choice == 'n':
                print(f"You didn't take the item")

            else:
                print(f"Bad panda! =(")
        return foundItems

    def __repr__(self):
        return f"name: {self.name}, description: {self.description}"
