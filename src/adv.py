from room import Room
from player import Player
from item import Item
from textwrap import TextWrapper

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                    "North of you, the cave mount beckons", 
                    ["lantern", "shovel", "hook"]), 

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["coin", "sword"]),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# print("This is the test", type(room['foyer']))
#
# Main
#
# player1 = Player('sean', 'outside')

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


###### VERSION 3 - figured out how to dynamically move around teh rooms
current_player = input(f"\n Enter your name to start the game!")
player1 = Player(current_player, room["outside"], [])

direction = input(f"""Please enter a direction:
[N]orth, [E]ast, [S]outh, [W]est, [Look], [I]nventory, [Q]uit:""")
Dir = direction.lower().strip()

currentRoom = "outside"

while not Dir == 'q':
    if Dir == "n" or Dir == "e" or Dir == "s" or Dir == "w":
        try:
            dirCall = (f"{Dir}_to")
            print(getattr(room[currentRoom], dirCall))

            currentRoom = getattr(room[currentRoom], dirCall).roomID

        except AttributeError:
            print(f"You can't go that way!")
    
    elif Dir == 'l':
        grabbedItems = room[currentRoom].look()
        for item in grabbedItems:
            player1.inventory.append(item)

    direction = input(f"""Please enter a direction:
[n], [e], [s], or [w] or [q] to quit:""")
    Dir = direction.lower().strip()





### VERSION 2 - works, but it long and not exactly the "right" way 
# def adventure_game():
#     # Prompt the user to type their name. 
#     player_name = input(f"\n Tell us your name, Player! \n Your name : ")
#     # Creates the Player instance
#     current_player = Player(player_name, "outside")
#     # Triggers the while loop below
#     playing = True
#     # Short message to the player
#     print(f"\n Hi {current_player.name}! Explore rooms and find treasure.")

#     while(playing):
#         # Allows me to access the dictionary and limit the text per line
#         wrapper = TextWrapper(width=70)
#         room_description = wrapper.wrap(
#             text=room[current_player.current_room].description)

#         # Shows the player which room they are in and the desc.
#         # Defaults to 'outside' on line 63
#         print(f"\n Current Room: \n {current_player.current_room}\n")
#         print(f"\n Room Description: \n")
#         for every_line in room_description:
#             print(every_line)
#         action = input(f"""Where do you want to go? (Use: n, e, s, or w). \n
# Type 'help' for a hint) : """)

#         if action == 'help':
#             print(f"""Type 'n' to move North, 'e' to move East, 'w' to move West,
# 's' to move South, 'help' for hints, or 'q' to end the game""")
#             action

#         if action == 'q':
#             exit()

#         if action == 'n':
#             if current_player.current_room == 'outside':
#                 current_player.current_room = "foyer"
#                 action
#             elif current_player.current_room == "foyer":
#                 current_player.current_room = "overlook"
#                 action
#             elif current_player.current_room == "narrow":
#                 current_player.current_room = "treasure"
#                 action
#             else:
#                 print(f"You can't go that way! Try again!")
#                 action

#         if action == 'e':
#             if current_player.current_room == "foyer":
#                 current_player.current_room = "narrow"
#                 action
#             else:
#                 print(f"You can't go that way! Try again!")
#                 action
        
#         if action == 's':
#             if current_player.current_room == "treasure":
#                 current_player.current_room = "narrow"
#                 action
#             elif current_player.current_room == "overlook":
#                 current_player.current_room = "foyer"
#                 action
#             elif current_player.current_room == "foyer":
#                 current_player.current_room = "outside"
#                 action
#             else:
#                 print(f"You can't go that way! Try again!")
#                 action

#         if action == 'w':
#             if current_player.current_room == "narrow":
#                 current_player.current_room = "foyer"
#                 action
#             else:
#                 print(f"You can't go that way! Try again!")
#                 action


# adventure_game()



### VERSION 1 - doesn't really work past 'help' and 'q'
# def adventure_game():
#     # Prompt the user to type their name. 
#     player_name = input(f"\n Tell us your name, Player! \n Your name : ")
#     # Creates the Player instance
#     current_player = Player(player_name, room["outside"])
#     # Triggers the while loop below
#     playing = True
#     # Short message to the player
#     print(f"\n Hi {current_player.name}! Explore rooms and find treasure.")

#     while(playing):
#         # Allows me to access the dictionary and limit the text per line
#         wrapper = TextWrapper(width=70)
#         room_description = wrapper.wrap(
#             text=room[current_player.current_room].description)

#         # Shows the player which room they are in and the desc.
#         # Defaults to 'outside' on line 63
#         print(f"\n Current Room: \n {current_player.current_room}\n")
#         print(f"\n Room Description: \n")
#         for every_line in room_description:
#             print(every_line)
#         action = input(f"""Where do you want to go? (Use: n, e, s, or w). \n
# Type 'help' for a hint) : """)

#         if action == 'help':
#             print(f"""Type 'n' to move North, 'e' to move East, 'w' to move West,
# 's' to move South, 'help' for hints, or 'q' to end the game""")

#         elif action == 'q':
#             exit()
        
#         elif action == 'n':
#             if current_player.current_room == room["outside"]:
#                 current_player.current_room == room["outside"].n_to
#                 # Room.n_to == room["foyer"]
#                 action
#             elif current_player.current_room == room["foyer"]:
#                 current_player.current_room == room["overlook"].n_to
#                 # Room.n_to == room["overlook"]
#                 action
#             elif current_player.current_room == room["overlook"]:
#                 print(f"Sorry, you can't go that way. Try again")
#                 action
