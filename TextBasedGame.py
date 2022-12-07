#Anabel Villalobos

#displays game instructions
def show_instructions():
   #print a main menu and the commands
   print("Vampire Text Adventure Game")
   print("Collect 6 items to win the game, or be killed by the vampire.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")


def playGame():
    # define rooms dictionary
    rooms = {
        'Living Room': {'North': 'Bedroom', 'West': 'Backyard', 'East': 'Laundry Room', 'South': 'Dining Room'},
        'Backyard': {'East': 'Living Room', 'item': 'stake'},
        'Bedroom': {'East': 'Bathroom', 'South': 'Living Room', 'item': 'apple'},
        'Bathroom': {'West': 'Bedroom', 'item': 'Vampire'},
        'Dining Room': {'North': 'Living Room', 'East': 'Kitchen', 'item': 'mirror'},
        'Kitchen': {'West': 'Dining Room', 'item': 'garlic'},
        'Laundry Room': {'West': 'Living Room', 'North': 'Garage', 'item': 'rosemary'},
        'Garage': {'South': 'Laundry Room', 'item': 'sunblade'}
    }

    # define user inventory as an empty list
    inventory = []
    # WHILE True:
    # 	IF the inventory length is equal to 6
    # 		RETURN “You have defeated the vampire!”
    # 	ELIF the currentRoom is equal to the “Bathroom”
    # 		RETURN “You see the vampire GAME OVER”
    # 	ELSE
    # 		run function for user input
    #
    # 	get user input for their move
    # 	split the array
    #
    # 	IF the first element in the array is not get or go
    # 		THEN print an error message


    # Pseudocode or Flowchart for Code to “Move Between Rooms”
    #
    # 	IF the first value in the array is “go”
    # 		IF the second value is in rooms.current_room
    # 			THEN set the current_room to equal rooms.current_room
    # 		ELSE
    # 			THEN PRINT “You can’t go that way”
    #
    # Pseudocode or Flowchart for Code to “Get an Item”
    #
    # 	IF the first element in the array is “get”
    # 		IF the second value is rooms.current_room.item
    # 			add this value into the inventory array
    # 			delete the item key in the rooms.current_room dictionary
    # 			PRINT “{Item} retrieved!”
    # 		ELSE
    # 			PRINT an error message


if __name__ == '__main__':
    show_instructions()
    playGame()

