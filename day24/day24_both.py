"""
Counts how many tiles are flipped to black.
Also flips tiles according to the rules for a given number of days.
"""

CODE_DICT = {
    "e": (0, 2),
    "w": (0, -2),
    "ne": (1, 1),
    "nw": (1, -1),
    "se": (-1, 1),
    "sw": (-1, -1)
}

def parse_input():
    """
    Processes user input. Each direction is given a specific value to make this
    hex grid, using the CODE_DICT above.
    """
    grid = {}
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            north = 0
            east = 0
            index = 0
            while index < len(line):
                code = ""
                char = line[index]
                if char == "s" or char == "n":
                    index += 1
                    code = line[index - 1] + line[index]
                else:
                    code = char
                to_add_north, to_add_east = CODE_DICT[code]
                north += to_add_north
                east += to_add_east
                index += 1
            coord = (north, east)
            flip_color (grid, coord)

    return grid

def flip_color(grid, coord):
    """
    Flips the color in the appropriate section of the hex grid.
    True = Black
    False = White
    """
    if not coord in grid:
        grid[coord] = True
        return
    grid[coord] = not grid[coord]

def count_black_tiles(grid):
    """
    Returns the number of black tiles up in the grid.
    """
    count = 0
    for coord in grid:
        if grid[coord]:
            count += 1

    return count

def living_art(grid):
    """
    Given a grid, flips tiles according to the following rules:
    - Black tiles with zero or more than 2 black tiles adjacent is flipped.
    - White tiles with exactly 2 black tiles adjacent is flipped.
    """
    to_flip = set()
    # First, set up the borders to be white
    add_borders(grid)
    for coord in grid:
        if grid[coord]: # This is a black tile
            blk_count = check_adjacency(grid, coord)
            if blk_count == 0 or blk_count > 2:
                to_flip.add(coord)
        else: # This is a white tile
            blk_count = check_adjacency(grid, coord)
            if blk_count == 2:
                to_flip.add(coord)
    for coord in to_flip:
        grid[coord] = not grid[coord]

    return grid

def add_borders(grid):
    """
    Given a particular coordinate, check the adjacent coords to it
    and if it does not exist yet in the grid dictionary, add it
    facing white.
    """
    to_add = set()
    for coord in grid:
        for adj in CODE_DICT:
            adj_coord = (coord[0] + CODE_DICT[adj][0],
                         coord[1] + CODE_DICT[adj][1])
            if not adj_coord in grid:
                to_add.add(adj_coord)
    for coord in to_add:
        grid[coord] = False

def check_adjacency(grid, coord):
    """
    Returns the number of black tiles immediately adjacent to this
    tile.
    """
    count = 0
    for adj in CODE_DICT:
        adj_coord = (coord[0] + CODE_DICT[adj][0],
                     coord[1] + CODE_DICT[adj][1])
        if adj_coord in grid:
            if grid[adj_coord]:
                count += 1

    return count

if __name__ == "__main__":
    grid = parse_input()
    print(f"There are {count_black_tiles(grid)} black tiles to start.")
    for counter in range (1, 101):
        grid = living_art(grid)
        print(f"Day {counter}: {count_black_tiles(grid)} black tiles.")