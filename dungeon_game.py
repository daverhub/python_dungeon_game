import random
CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_location(arg):
    # monster =  random
    # door = random
    # start = random

    # if monster, door , or start are the same do it again
def move_player(player, move):
    # Get player's current location
    # If move is LEFT y - 1
    # If move is RIGHT y + 1
    # If move is UP x - 1
    # If move is Down x + 1
def get_moves(player, move):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # if player's y i 0 remove LEFT
    # if player's x i 0 remove LEFT
    # if player's y i 2 remove LEFT
    # if player's x i 0 remove LEFT
while True:
    print("Welcome to the dungeon!")
    print("You're current;y in room {}")
    print("You can move {}")
    print("ENTER QUIT to quit")

    move = raw.input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
