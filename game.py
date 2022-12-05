

def game():
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