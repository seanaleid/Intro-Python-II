from room import Room
from player import Player
from textwrap import TextWrapper

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


def adventure_game():
    # Prompt the user to type their name. 
    player_name = input(f"\n Tell us your name, Player! \n Your name : ")
    # Creates the Player instance
    current_player = Player(player_name, "outside")
    # Triggers the while loop below
    playing = True
    # Short message to the player
    print(f"\n Hi {current_player.name}! Explore rooms and find treasure.")

    while(playing):
        # Allows me to access the dictionary and limit the text per line
        wrapper = TextWrapper(width=70)
        room_description = wrapper.wrap(
            text=room[current_player.current_room].description)

        # Shows the player which room they are in and the desc.
        # Defaults to 'outside' on line 63
        print(f"\n Current Room: \n {current_player.current_room}\n")
        print(f"\n Room Description: \n")
        for every_line in room_description:
            print(every_line)
        action = input(f"""Where do you want to go? (Use: n, e, s, or w. \n
Type 'help' for a hint) : """)

        if action == 'help':
            print(f"""Type 'n' to move North, 'e' to move East, 'w' to move West,
's' to move South, 'help' for hints, or 'q' to end the game""")

        elif action == 'q':
            exit()
    # print(f"Your are currently in {player1.current_room}")
    # if player1.current_room == 'outside':
    #     print(room['outside'].description)


adventure_game()
