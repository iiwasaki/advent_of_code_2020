def highest_seat_id():
    highest_id = 0
    with open("input.txt", "r") as input_file:
        for line in input_file:
            highest_id = max(resolve_id(line), highest_id)
    print (highest_id)

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
    highest_seat_id()