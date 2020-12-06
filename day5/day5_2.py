"""
This assumes that we have already resolved Part 1, and we know
the highest number on a boarding pass.
"""

def find_my_seat():
    max_seat_id = 915
    seats_map = []
    for i in range(max_seat_id):
        seats_map.append(0)
    with open("input.txt", "r") as input_file:
        for line in input_file:
            seat_id = resolve_id(line)
            if seat_id == -1:
                return -1 # Failed to parse a seat properly
            seats_map[seat_id-1] = 1
    for i in range(1, max_seat_id):
        if seats_map[i] == 0:
            if seats_map[i-1] == 1 and seats_map[i+1] == 1:
                return i+1
    return -1 #Failed to find a seat

def resolve_id(seat_code):
    """
    Takes in a seat code in the format XXXXXXXYYY
    where X is F or B and Y is L or R, and then returns
    the ID number of that seat.
    """
    if len(seat_code) != 11:
        return -1
    lower_bound_row = 0
    upper_bound_row = 127
    lower_bound_col = 0
    upper_bound_col = 7
    # Not perfect error checking here, should check that only the last 3
    # chars are L/R and that only the first 7 are F/B...
    for character in seat_code:
        if character == "F":
            upper_bound_row = (upper_bound_row + lower_bound_row) // 2
        elif character == "B":
            lower_bound_row = (upper_bound_row + lower_bound_row) // 2
        elif character == "L":
            upper_bound_col = (upper_bound_col + lower_bound_col) // 2
        elif character == "R":
            lower_bound_col = (upper_bound_col + lower_bound_col) // 2
        elif character == "\n":
            pass
        else:
            return -1 #Invalid character
    return (upper_bound_row * 8) + upper_bound_col

if __name__ == "__main__":
    print (find_my_seat())