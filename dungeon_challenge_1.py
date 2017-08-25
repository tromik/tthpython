# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    r, t = direction

    new_x = x + r
    new_y = y + t

    if new_x < 0 or new_x > 9 or new_y < 0 or new_y > 9:
        hp -= 5
    else:
        x, y = new_x, new_y

    return x, y, hp

print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))
