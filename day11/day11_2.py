"""
A redone version of day11_1.py with the new rules for
reaching seat equilibrium.
"""

import copy


def simulate_seating(seats):
    """
    Simulate people entering the ferry as many times as necessary
    until the seats stop changing according to the rules.
    """
    num_rows = len(seats)
    num_cols = len(seats[0])
    modified_seats = copy.deepcopy(seats)
    while True:
        changed = False

        # For every seat, check the seat
        for rows in range (0, num_rows):
            for cols in range (0, num_cols):
                if seats[rows][cols] == ".":
                    continue # If it's a floor, do nothing
                occupied_count = count_occupied(seats, rows, cols)

                # Apply the first rule: if seat is empty and nobody around is
                # occupied, fill it.
                if seats[rows][cols] == "L":
                    if occupied_count == 0:
                        modified_seats[rows][cols] = "#"
                        changed = True

                # Apply the second rule: if seat is filled, empty it if
                # four or more seats adjacent are empty.
                elif seats[rows][cols] == "#":
                    if occupied_count >= 5:
                        modified_seats[rows][cols] = "L"
                        changed = True
        if not changed:
            break
        seats = copy.deepcopy(modified_seats)

    # seats_copy has the final seating arrangements
    occupied_seats = 0
    for line in seats:
        for seat in line:
            if seat == "#":
                occupied_seats += 1

    return occupied_seats

def count_occupied(seats, row, col):
    """
    Return how many seats are occupied around the given seat,
    now resolving for the first seat seen in a given direction.
    """
    occupied = 0
    occupied += return_seat(seats, row, col, -1, 0)
    occupied += return_seat(seats, row, col, +1, 0)
    occupied += return_seat(seats, row, col, 0, +1)
    occupied += return_seat(seats, row, col, 0, -1)
    occupied += return_seat(seats, row, col, +1, -1)
    occupied += return_seat(seats, row, col, +1, +1)
    occupied += return_seat(seats, row, col, -1, -1)
    occupied += return_seat(seats, row, col, -1,+ 1)

    return occupied

def return_seat(seats, row, col, row_mod, col_mod):
    """
    Returns the first seat seen in the particular direction of where
    we are looking.
    """
    row += row_mod
    col += col_mod
    while row >= 0 and col >= 0:
        try:
            seat = seats[row][col]
            if seat == "#":
                return 1
            if seat == "L":
                return 0
        except IndexError:
            return 0
        row += row_mod
        col += col_mod
    return 0

def parse_input():
    """
    Parses the input file and returns a list of strings.
    """
    input_list = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.rsplit("\n", 1)
            input_list.append(list(line[0]))

    return input_list

def print_seats(seats):
    """
    Helper function during testing to print out the seats in a
    more visible way.
    """
    for line in seats:
        print (str(line))
        print ()

if __name__ == "__main__":
    dataset = parse_input()
    print(simulate_seating(dataset))
