# Adam Sawyer
# Text Based Game

# room dictionary
# contains a list of all the rooms and the directions where a new room can be found
station_dict = {
    'Shuttle Bay': {
        'south': 'Service Room',
        'north': '',
        'east': '',
        'west': '',
        'item': ''
    },
    'Service Room': {
        'south': 'Garden',
        'north': 'Shuttle Bay',
        'east': 'Radio Room',
        'west': 'Control Room',
        'item': 'Observatory key'
    },
    'Radio Room': {
        'south': '',
        'north': '',
        'east': '',
        'west': 'Service Room',
        'item': 'Portable radio'
    },
    'Control Room': {
        'south': '',
        'north': '',
        'east': 'Service Room',
        'west': '',
        'item': 'Access card'
    },
    'Garden': {
        'south': 'Laboratory',
        'north': 'Service Room',
        'east': '',
        'west': '',
        'item': 'Apple'
    },
    'Laboratory': {
        'south': 'Observatory',
        'north': 'Garden',
        'east': 'Storage locker',
        'west': 'Armory',
        'item': 'Helium-argon laser'
    },
    'Storage locker': {
        'south': '',
        'north': '',
        'east': '',
        'west': 'Laboratory',
        'item': 'space suit'
    },
    'Armory': {
        'south': '',
        'north': '',
        'east': 'Laboratory',
        'west': '',
        'item': 'laser pistol'
    },
    'Observatory': {
        'south': '',
        'north': 'Laboratory',
        'east': '',
        'west': '',
        'item': 'alien'
    }
}
current_room = 'Shuttle Bay'
full_inventory = {
                      '1': 'Observatory key',
                      '2': 'Portable radio',
                      '3': 'Access card',
                      '4': 'Apple',
                      '5': 'Helium-argon laser',
                      '6': 'space suit',
                      '7': 'laser pistol',
                  }
inventory = []
command = ''


# initial instructions to the player about how to play the game
def show_instructions():
    # print(station_dict)
    title = "Space Station Rescue Game"
    # I wanted the name of the game to stand out, so I called upper() on a pre-written string
    print(title.upper())

    print("Collect all seven (7) items to win the game, or be killed by the hostile alien.")
    print("Move commands: move south, move north, move east, move west")
    print("Add to Inventory: get 'item name'")
    print("Display items in inventory: show items")


def show_room(room):
    print('\n' + 'Your are currently in the ' + room)


def show_inventory():
    print('Inventory: ', inventory)
    print('--------------------' + '\n')


def user_status(): #indicate room and inventory contents
    print('\n-------------------------')
    print('You are in the {}'.format(current_room))
    print('In this room you see {}'.format(station_dict[current_room]['item']))
    print('Inventory:', inventory)
    print('-------------------------------')


def valid_direction():
    print('Valid direction')


def invalid_direction():
    print('You have chosen poorly. Pick another direction to move')


def legal_move(direction):
    print('You can move in the direction of ' + direction + ' from the ' + current_room)


def illegal_move(direction):
    print('You CANNOT move in the direction of ' + direction + ' from the ' + current_room)


def start_game():
    # this is the final room that should be entered
    # while we are not at the end of the game or the last room with the alien
    while current_room != 'Observatory':
        user_status()
        command = input('Enter an action to take: ').lower()
        print("Command: " + command)
        command_zero = command.split(" ")[0]
        command_one = command.split(" ")[1]
        print("Index 0: " + command_zero)
        print("Index 1: " + command_one)

        if command_zero == 'move':
            print('Player has asked to move')
            direction = command_one
            print("Direction: " + direction)
            cardinal_values = station_dict[current_room].keys()
            print(cardinal_values)
            available_rooms = station_dict[current_room].values()
            print(available_rooms)

            if direction in station_dict[current_room][direction] != '':
                print('User can move in the direction of ' + direction + ' from the ' + current_room)
            else:
                print('You cannot move in the direction of ' + direction + ' from the ' + current_room)
        elif command_zero == 'get':
            print('Player wants to get an item')
            item = command_one
            if item in station_dict[current_room]['item']:
                inventory.append(item)
                show_inventory()
            print("Item: " + item)
        else:
            print('You have entered an invalid move')


if __name__ == '__main__':
    # Show the initial instructions to the user when the game starts
    show_instructions()

    # Display their starting position
    show_room(current_room)

    # Display the starting inventory
    show_inventory()

    start_game()
