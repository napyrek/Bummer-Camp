location = 'Basketball Court' # sets start location
inventory = [] # creates inventory

def intro():
    # print instructions
        print('Welcome to Summer Camp\n'
               'Collect all 6 items to catch the killer.')
        print('To move through camp: go North, go South, go East, go West')
        print('To add an item to your inventory: get "item name"')
        print('----------------------------------------------------------')
        start()
        # starts start() function

def start():
    # displays inventory and starts game
    global inventory
    global location
    print('Inventory:', inventory)
    print('You are at the {}.'.format(location))
    print('----------------------------------------------------------')
    main()
    # starts main() gameplay loop
def main():
    # gameplay loop
    global location
    global inventory
    rooms = {
        'Cabin': {'East': 'Infirmary', 'West': 'Dining Hall', 'item': 'Flashlight'},
        'Infirmary': {'West': 'Cabin', 'South': 'Lake', 'item': 'Bandage'},
        'Lake': {'West': 'Basketball Court', 'North': 'Infirmary', 'South': 'Rock Climbing Wall', 'item': 'Paddle'},
        'Rock Climbing Wall': {'North': 'Lake', 'West': 'Amphitheater', 'item': 'Rope'},
        'Amphitheater': {'North': 'Archery Range', 'East': 'Rock Climbing Wall', 'item': 'Killer'}, # villain
        'Archery Range': {'North': 'Dining Hall', 'East': 'Basketball Court', 'South': 'Amphitheater', 'item': 'Bow & Arrow'},
        'Dining Hall': {'South': 'Archery Range', 'East': 'Cabin', 'item': 'Sandwich'},
        'Basketball Court': {'North': 'Cabin', 'East': 'Lake', 'West': 'Archery Range'}
    }

    while True:
        player_move = input('Which way do you go? ').split()[-1].capitalize()  # if user enters input in all lower case program will capitalize first character of second word displays current room
        print('----------------------------------------------------------')
        if player_move in rooms[location]: # input validation
            print('You are now at the', rooms[location][player_move]) # displays current room
            location = rooms[location][player_move]
            print('Inventory:', inventory)

            if 'item' in rooms[location]:
                item = rooms[location]['item']
                print('You see a', rooms[location]['item'])
                if item == 'Killer':
                    if len(inventory) == 6:
                        print('You caught the killer!\nCongratulations!')
                        break
                    else:
                        print('You were not prepared!\nYou were killed!\nGame over!')
                        break
                get_item = input('Get item? ').split()[-1].capitalize()
                print('----------------------------------------------------------')
                if get_item in rooms[location]['item']:
                    if item in inventory:
                        print('You already have this item!')
                    else:
                        inventory.append(item)
                        print('Inventory:', inventory)
                else:
                    print('Invalid move')
        else:
            print('Invalid direction')

intro()
