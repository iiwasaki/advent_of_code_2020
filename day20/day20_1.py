from math import sqrt
from copy import deepcopy

class Tile:
    def __init__(self, id_num):
        """
        Initializes the tile object
        """
        self.locked = False
        self.id = id_num
        self.grid = []
        self.top = ""
        self.right = ""
        self.bottom = ""
        self.left = ""
        self.top_con = None
        self.bottom_con = None
        self.left_con = None
        self.right_con = None

    def define_grid(self, grid):
        self.right = ""
        self.left = ""
        self.grid = grid
        self.top = grid[0]
        self.bottom = grid[len(grid) - 1]
        for line in self.grid:
            self.left = self.left + line[0]
            self.right = self.right + line[len(line) - 1]

    def rotate(self):
        new_grid = []
        for index in range(0, len(self.grid[0])):
            new_line = ""
            for line in self.grid:
                new_line = line[index] + new_line
            new_grid.append(new_line)
        self.define_grid(new_grid)

    def flip(self):
        new_grid = []
        for line in self.grid:
            new_grid.insert(0, line)
        self.define_grid(new_grid)

    def strip_borders(self):
        new_grid = []
        for line in self.grid:
            new_line = line[1:len(line)-1]
            new_grid.append(new_line)
        new_grid = new_grid[1:len(new_grid) - 1]
        self.define_grid(new_grid)


    def print_tile(self):
        print(f"Tile ID: {self.id}")
        for line in self.grid:
            print (line)
        print()
        print(f"Right: {self.right}")
        print(f"Left: {self.left}")
        print(f"Top: {self.top}")
        print(f"Bottom: {self.bottom}")
        print()

    def print_connections(self):
        print()
        print(f"Tile ID: {self.id}")
        if self.right_con:
            print(f"Right tile ID: {self.right_con.id}")
        else:
            print("No right connection.")
        if self.left_con:
            print(f"Left tile ID: {self.left_con.id}")
        else:
            print("No left connection.")
        if self.bottom_con:
            print(f"Bottom tile ID: {self.bottom_con.id}")
        else:
            print("No bottom connection.")
        if self.top_con:
            print(f"Top tile ID: {self.top_con.id}")
        else:
            print("No top connection")
        print()


def parse_input():
    tile_set = set()
    with open("input.txt", "r") as input_file:
        tile_id = -1
        tile_grid = []
        for line in input_file:
            if line[0] == "T":
                line = str(line.split(" ", 1)[1])
                line = line.split(":")[0]
                tile_id = int(line)
            elif line == "\n":
                if tile_id != -1:
                    tile = Tile(tile_id)
                    tile.define_grid(tile_grid)
                    tile_set.add(tile)
                    tile_id = -1
                    tile_grid = []
            else:
                line = line.strip("\n")
                tile_grid.append(line)

    return tile_set

def find_match(tile, tileset):
    find_right(tile, tileset)
    find_left(tile, tileset)
    find_top(tile, tileset)
    find_bottom(tile, tileset)

def find_right(tile, tileset):
    if tile.right_con:
        return
    match_right(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_right(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_right(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_right(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_right(tile, tileset)

def find_top(tile, tileset):
    if tile.top_con:
        return
    match_top(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_top(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_top(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_top(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_top(tile, tileset)

def find_bottom(tile, tileset):
    if tile.bottom_con:
        return
    match_bottom(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_bottom(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_bottom(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_bottom(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_bottom(tile, tileset)

def find_left(tile, tileset):
    if tile.left_con:
        return
    match_left(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_left(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_left(tile, tileset)
    if not tile.locked:
        tile.rotate()
        match_left(tile, tileset)
    if not tile.locked:
        tile.flip()
        match_left(tile, tileset)

def match_right(tile, tileset):
    for target in tileset:
        if target.left == tile.right:
            if target.left_con:
                print ("Already have left con?")
                return
            else:
                tile.right_con = target
                target.left_con = tile
                tile.locked = True
                target.locked = True
                return

def match_left(tile, tileset):
    for target in tileset:
        if target.right == tile.left:
            if target.right_con:
                print ("Already have right con?")
                return
            else:
                tile.left_con = target
                target.right_con = tile
                tile.locked = True
                target.locked = True
                return

def match_top(tile, tileset):
    for target in tileset:
        if target.bottom == tile.top:
            if target.bottom_con:
                print ("Already have down con?")
                return
            else:
                tile.top_con = target
                target.bottom_con = tile
                tile.locked = True
                target.locked = True
                return

def match_bottom(tile, tileset):
    for target in tileset:
        if target.top == tile.bottom:
            if target.top_con:
                print ("Already have up con?")
                return
            else:
                tile.bottom_con = target
                target.top_con = tile
                tile.locked = True
                target.locked = True
                return

def resolve_tiles(tileset):
    print ("Creating square...")
    for tile in tileset:
        print(f"Checking square starting at tile ID {tile.id}")
        for _ in range(0, 4):
            return_sq = create_square(tile, tileset)
            if return_sq:
                return return_sq
            tile.flip()
            reset_tiles(tileset)
            return_sq = create_square(tile, tileset)
            if return_sq:
                return return_sq
            tile.flip()
            tile.rotate()
            reset_tiles(tileset)

    return None

def reset_tiles(tileset):
    for tile in tileset:
        tile.top_con = None
        tile.bottom_con = None
        tile.left_con = None
        tile.right_con = None

def create_square(topleft, tileset):
    sidelen = int(sqrt(len(tileset)))
    side_index = 0
    square = [[topleft]]
    square_ids = {topleft.id}
    while len(square_ids) < len(tileset):
        found = False
        for tile in tileset:
            if tile.id in square_ids:
                continue
            if len(square_ids) % sidelen == 0:
                # Look down
                curr = square[side_index][0]
                for _ in range(0, 4):
                    if curr.bottom == tile.top:
                        curr.bottom_con = tile
                        tile.top_con = curr
                        side_index += 1
                        square.append([tile])
                        square_ids.add(tile.id)
                        found = True
                        break
                    tile.flip()
                    if curr.bottom == tile.top:
                        curr.bottom_con = tile
                        tile.top_con = curr
                        side_index += 1
                        square.append([tile])
                        square_ids.add(tile.id)
                        found = True
                        break
                    tile.flip()
                    tile.rotate()
            else:
                # Look right
                curr = square[side_index][len(square[side_index]) - 1]
                for _ in range(0, 4):
                    if curr.right == tile.left:
                        square[side_index].append(tile)
                        curr.right_con = tile
                        tile.left_con = curr
                        if side_index > 0:
                            current_index = len(square[side_index])
                            tile.top_con = square[side_index-1][current_index - 1]
                            square[side_index-1][current_index - 1].bottom_con = tile
                        square_ids.add(tile.id)
                        found = True
                        break
                    tile.flip()
                    if curr.right == tile.left:
                        curr.right_con = tile
                        tile.left_con = curr
                        square[side_index].append(tile)
                        if side_index > 0:
                            current_index = len(square[side_index])
                            tile.top_con = square[side_index-1][current_index - 1]
                            square[side_index-1][current_index - 1].bottom_con = tile
                        square_ids.add(tile.id)
                        found = True
                        break
                    tile.flip()
                    tile.rotate()
        if not found:
            return None
    if len(square_ids) == len(tileset):
        return square
    print ("Why we here?")
    return None

def combine_image(square):
    picture_list = []
    process_borders(square)
    string = ""
    string = string + (square[0][0].top)
    string = string + (square[0][1].top)
    string = string + (square[0][2].top)
    square_len = len(square)
    inner_sq_len = len(square[0])
    grid_len = len(square[0][0].grid)
    for sq_index in range(0, square_len):
        for grid_ix in range(0, grid_len):
            line = ""
            for in_sq_ix in range(0, inner_sq_len):
                line = line + square[sq_index][in_sq_ix].grid[grid_ix]
            picture_list.append(line)
    return (picture_list)

def print_image(picture_list):
    for line in picture_list:
        print(line)

def find_sea_monster(picture_list):
    first_row = [-18, -13, -12, -7, -6, -1, 0, 1]
    second_row = [-17, -14, -11, -8, -5, -2]
    num_lines = len(picture_list)
    monsters = 0
    for line_ix in range(0, num_lines-2):
        line = picture_list[line_ix]
        line_max = len(line)
        for index in range (17, line_max):
            if line[index] == "#":
                monster = True
                for num in first_row:
                    if not picture_list[line_ix+1][num + index] == "#":
                        monster = False
                        break
                if not monster:
                    continue
                for num in second_row:
                    if not picture_list[line_ix+2][num + index] == "#":
                        monster = False
                        break
                if monster:
                    monsters += 1

    return monsters

def rotate_picture(picture):
    new_grid = []
    for index in range(0, len(picture)):
        new_line = ""
        for line in picture:
            new_line = line[index] + new_line
        new_grid.append(new_line)
    return new_grid

def flip_picture(picture):
    new_grid = []
    for line in picture:
        new_grid.insert(0, line)
    return new_grid

def process_borders(square):
    for line in square:
        for tile in line:
            tile.strip_borders()

def count_sharps(picture):
    sharps = 0
    for line in picture:
        for char in line:
            if char == "#":
                sharps += 1

    return sharps


if __name__ == "__main__":
    tile_set = parse_input()
    square = resolve_tiles(tile_set)
    topleft = square[0][0].id
    topright = square[0][len(square[0]) - 1].id
    bottomleft = square[len(square) - 1][0].id
    bottomright = square[len(square) - 1][len(square[0]) - 1].id
    product = bottomright * bottomleft * topleft * topright
    print (f"Product of corners is {product}")
    sidelen = int(sqrt(len(square)))
    picture = combine_image(square)
    for _ in range(0, 4):
        picture = rotate_picture(picture)
        monsters = find_sea_monster(picture)
        print (monsters)
        picture = flip_picture(picture)
        monsters = find_sea_monster(picture)
        print (monsters)
        picture = flip_picture(picture)
    num_sharps = count_sharps(picture)
    print(num_sharps - (16 * 15))