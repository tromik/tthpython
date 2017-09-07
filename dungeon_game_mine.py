import os
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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    # get player position and move
    # return new player position
    x, y = player

    if move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1
    elif move == "UP":
        y -= 1
    elif move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    # get player position
    # return valid moves so the player cannot exit the game grid
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player

    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    return moves


def draw_map(player, monster=None, exit=None):
    print(" _" * 5)
    tile = "|"
    tile_bottom = "_"
    player_icon = "X"
    monster_icon = "M"
    exit_icon = "D"
    tile_construct = "{}{}{}"

    for cell in CELLS:
        x, y = cell

        if x < 4:
            line_end = ""
            tile_wall = ""
        else:
            line_end = "\n"
            tile_wall = "|"

        if cell == exit:
            output = tile_construct.format(tile, exit_icon, tile_wall)
        elif cell == monster:
            output = tile_construct.format(tile, monster_icon, tile_wall)
        elif cell == player:
            output = tile_construct.format(tile, player_icon, tile_wall)
        else:
            output = tile_construct.format(tile, tile_bottom, tile_wall)


        print(output, end=line_end)




def game_loop():
    monster, exit, player = get_locations()

    while True:
        clear_screen
        print()
        draw_map(player)
        print("You are currently in room {}".format(player)) # add position

        available_moves = get_moves(player)
        print("You can move {}, or enter QUIT to exit the game".format(", ".join(available_moves))) # add available moves

        move = input("> ").upper()

        if move == "QUIT" or move == "EXIT":
            break

        if move == "CHEAT":
            clear_screen()
            print()
            draw_map(player=player, monster=monster, exit=exit)
            print()
            print("Monster: {}".format(monster))
            print("Exit: {}".format(exit))
            input("Press RETURN or ENTER to continue")

        # good move? move the player
        if move in available_moves:
            player = move_player(player, move)
        # bad move? Don't do anything
        else:
            input("{} is not a valid move. You can move {} Press enter to continue.".format(move, ", ".join(available_moves)))
            clear_screen()

        if player == exit:
            # on the exit? win
            clear_screen()
            print()
            draw_map(player=player, exit=exit)
            print()
            print("you win")
            break

        if player == monster:
            # on the monster? lose
            clear_screen()
            print()
            draw_map(player=player, monster=monster)
            print()
            print("You lose")
            break

    # otherwise loop


def game_start():
    clear_screen()
    print("Wecome to Dungeon Game!")
    print("-----------------------")
    print()
    input("Press RETURN or ENTER to start")
    clear_screen()
    game_loop()


game_start()
