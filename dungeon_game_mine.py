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

print(random.sample(CELLS, 1)[0])

def get_locations():
    monster = random.sample(CELLS, 1)[0]
    exit = random.sample(CELLS, 1)[0]
    player = random.sample(CELLS, 1)[0]

    return monster, exit, player


def move_player(player, move):
    # get player position
    x, y = player

    if move == "LEFT":
        # if move == LEFT, x - 1
        x -= 1
    elif move == "RIGHT":
        # if move == RIGHT, x + 1
        x += 1
    elif move == "UP":
        # if move == UP, y - 1
        y -= 1
    elif move == "DOWN":
        # if move == DOWN, y + 1
        y += 1
    # return new player position
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    # if players y == 0, they can't move UP
    if y == 0:
        moves.remove("UP")
    # if players y == 4, they can't move DOWN
    if y == 4:
        moves.remove("DOWN")
    # if players x == 0, they can't move LEFT
    if x == 0:
        moves.remove("LEFT")
    # if players x == 4, they can't move RIGHT
    if x == 4:
        moves.remove("RIGHT")
    return moves



monster, exit, player = get_locations()

while True:

    print("You are currently in room {}".format(player)) # add position

    available_moves = get_moves(player)
    print("You can move {}, or enter QUIT to exit the game".format(available_moves)) # add available moves

    move = input("> ").upper()

    if move == "QUIT":
        break

    if move == "CHEAT":
        print("Monster: {}".format(monster))
        print("Exit: {}".format(exit))

    # good move? move the player
    if move in available_moves:
        player = move_player(player, move)
    # bad move? Don't do anything
    else:
        print("{} is not a valid move. You can move {}".format(move, available_moves))

    if player == exit:
        # on the exit? win
        print("you win")
        break

    if player == monster:
        # on the monster? lose
        print("You lose")
        break

    # otherwise loop
