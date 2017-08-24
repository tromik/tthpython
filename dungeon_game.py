import random

# Create a game with a 2-dimensional map.
# Place the player, a door, and a monster into random spots in your map.
# Let the player move around in the map and, after each move,
# tell them if they've found the door or the monster.
# If they find either the game is over.
# The door is the win condition, the monster is the lose condition.

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player on the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear the screen and redraw the grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def get_locations():
    monster = None
    exit = None
    player = None

    return monster, exit, player


def move_player(player, move):
    # get player position
    # if move == LEFT, x - 1
    # if move == RIGHT, x + 1
    # if move == UP, y - 1
    # if move == DOWN, y + 1
    # return new player position
    return player


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    # if players y == 0, they can't move UP
    # if players y == 4, they can't move DOWN
    # if players x == 0, they can't move LEFT
    # if players x == 4, they can't move RIGHT

while True:
    print("Welcome to the dungeon!")
    print("You are currently in room {}".format()) # add position
    print("You can move {}".format()) # add available moves
    print("Enter QUIT to quit the game")

    move = input("> ").upper()

    # good move? move the player
    # bad move? Don't do anything
    # on the exit? win
    # on the monster? lose
    # otherwise loop
