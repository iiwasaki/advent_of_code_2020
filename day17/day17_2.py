"""
Simulates six cycles of this cube bootup.. thing? Now in 4D!
"""

from modifier_sets import MODIFIER_SET_4D

def resolve_cycles(num_cycles, active):
    """
    Performs the rules for this cube game for a given number
    of cycles.
    Active cubes: Stays active if 2 or 3 neighbors also active.
                  Otherwise, become inactive.
    Inactive cubes: Turns active if 3 of its neighbors are active.
                    Otherwise, stay inactive.
    num_cycles is the nubmer of times to run the rules.
    active is the set of coordinates for active cubes.
    """
    for _ in range (0, num_cycles):
        active_neighbors = {}
        to_remove = set()
        for coords in active:
            active_rule(coords, to_remove, active)
            fill_neighbors(coords, active_neighbors, active)
        for coords in to_remove:
            active.remove(coords)
        for coords in active_neighbors:
            if active_neighbors[coords] == 3:
                active.add(coords)

    print(len(active))

def fill_neighbors(cube, active_neighbors, active):
    """
    Takes an active cube and increments the count in the
    active_neighbors dictionary for every inactive member.
    """
    x_coord = cube[0]
    y_coord = cube[1]
    z_coord = cube[2]
    w_coord = cube[3]
    for modifier in MODIFIER_SET_4D:
        neighbor_coords = (x_coord + modifier[0],
                        y_coord + modifier[1],
                        z_coord + modifier[2],
                        w_coord + modifier[3])
        if neighbor_coords in active:
            continue # Do nothing since it's an active neighbor
        if neighbor_coords in active_neighbors:
            active_neighbors[neighbor_coords] += 1
        else:
            active_neighbors[neighbor_coords] = 1

    return

def active_rule(cube, to_remove, active):
    """
    Process the rules for a given cube that is active.
    If it does not follow the rules, add it to the to_remove
    set.
    """
    x_coord = cube[0]
    y_coord = cube[1]
    z_coord = cube[2]
    w_coord = cube[3]
    adj_actives = 0 # Keeps track of neighbor active cubes
    for modifier in MODIFIER_SET_4D:
        adj_actives += is_active(x_coord + modifier[0],
                                y_coord + modifier[1],
                                z_coord + modifier[2],
                                w_coord + modifier[3],
                                active)
        if adj_actives > 3:
            to_remove.add(cube)
            return

    if adj_actives < 2:
        to_remove.add(cube)

    return

def is_active(x, y, z, w, active):
    """
    Returns a 1 if the coordinates are in the active set,
    0 if not.
    """
    if (x, y, z, w) in active:
        return 1

    return 0

def process_input():
    """
    Process the input text. Returns a set of coordinates
    for those cubes that are active.
    """
    active = set()
    with open("input.txt", "r") as input_text:
        z = 0
        w = 0
        y = 0
        for line in input_text:
            for index, char in enumerate(line):
                if char == "#":
                    active.add((index, y, z, w))
            y += 1

    return active


if __name__ == "__main__":
    first_active = process_input()
    resolve_cycles(6, first_active)