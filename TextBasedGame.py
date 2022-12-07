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
    current_room = 'Living Room'
    # define user inventory as an empty list
    inventory = []

    while True:
        # if the player entered exit
        if current_room.lower() == 'exit':
            # exit the game
            print("Thanks for playing the game. Hope you enjoyed it.")
            break
        # if the player picked up the last item
        if len(inventory) == 6:
            # exit the game
            print("Congratulations! You have collected all items and defeated the vampire!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break
        # if the player enters the room with the vampire
        elif current_room == "Bathroom":
            # exit the game
            print("HISSSS GAME OVER")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break
        else:
        # continue with the game
            print("You are in the {}".format(current_room))
            print("Inventory: {}".format(inventory))
            if 'item' in rooms[current_room]:
                print("You see a {}".format(rooms[current_room]['item']))
            print("----------------------------------")
            print("Enter your move")

            #otherwise get new user input
            player_move = input()

            # 	split into array
            move_arr = player_move.split(" ")

            if move_arr[0] == "go":
                direction = move_arr[1]
                # if the direction is in the current room dictionary
                if direction in rooms[current_room]:
                    # set the current room equal to that room
                    current_room = rooms[current_room][direction]
                else:
                    print("You can't go that way")
            elif move_arr[0] == "get":
                current_item = move_arr[1]
                # if the item is in the current room
                if rooms[current_room]['item'] == current_item:
                    # add the item to the inventory
                    # add this value into the inventory array
                    inventory.append(current_item)
                    # delete the item key in the rooms.current_room dictionary
                    del rooms[current_room]['item']
                    print(rooms[current_room])
                else:
                    print("Can't get {}!".format(current_item))


            # if the player input is exit
            elif move_arr[0].lower() == "exit":
                # then the current room is set to exit
                current_room = "exit"
            else:
                # handle input validation error
                print("Invalid command")








if __name__ == '__main__':
    show_instructions()
    playGame()

