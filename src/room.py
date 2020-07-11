# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomID, name, description, items):
        self.roomID = roomID
        self.name = name
        self.description = description
        self.items = items

    def look(self):
        foundItems = []
        for item in self.items:
            # itemName = item
            print(f"\n\tYou found {item}")
            choice = input(f"\n\tDo you want to take it? y/n ")

            if choice == 'y':
                print(f"\n\t{item[0].upper} added to your inventory")
                self.items.remove(item)
                foundItems = item
                break
                # print(player1.inventory)
            
            elif choice == 'n':
                print(f"\n\tYou didn't take the item")
                break

            else:
                print(f"\nBad panda! =(")
        return foundItems

    def __repr__(self):
        return f"name: {self.name}, description: {self.description}"
