TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    line = "{}".format(tile)
    line_end = ""
    if tile == '||':
        line = ""
        line_end = "\n"
    print(line, end=line_end)
