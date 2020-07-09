# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f"name: {self.name}, current_room: {self.current_room}"

    def get(self, item):
        pass
    
    def drop(self, item):
        pass
