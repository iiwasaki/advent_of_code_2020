"""
Figures out the earliest timestamp such that all of the listed
Bus IDs depart at offsets matching their positions in the list.
"""

def matching_offsets(id_list):
    """
    Figures out the earliest timestamp given a list of Bus IDs that
    satisfies all of the listed Bus IDs departing at the correct offsets.
    This assumes the first value in the list is not an "X".
    The reasoning for the algorithm is such:
        Starting at the top of the list, find multiples of the first value
        until we arrive at a number that satisfies the offset thing for the
        next number on the list.
        For those 2 numbers, the offset thing will hold true for every
        time that is (time + (product of the 2 numbers)). For example, if
        the list has [7, 13, 51] then 7 and 13 first meet at time = 77.
        77 is when bus 7 departs, 78 is when bus 13 departs.
        7 * 13 = 91, and we see that 77 + 91 = 168 also satisfies the
        conditions, as does 168 + 91, and so on. That 91 is our
        "increment" variable.
        So, we build upon that, starting at 77, adding 91 until we find
        a time that satisfies the ID 51, offset 2, condition as well.
        We then multiply the 51 to the 91 to create the new increment, and
        continue as necessary until the end of the list.
    """
    increment = id_list[0]
    time = 0
    for index in range(1, len(id_list)):
        if isinstance(id_list[index], str):
            continue
        while True:
            time += increment
            if (time + index) % id_list[index] == 0:
                increment *= id_list[index]
                break
    return time


def parse_input():
    """
    Reads the input and returns it in a list form where the
    bus IDs are in the list, and the index is the offset. X's are
    allowed in this one.
    """
    id_list = []
    with open("input.txt", "r") as input_file:
        line = input_file.readlines()[1].split(',')
        for bus_id in line:
            try:
                bus_id = int(bus_id)
                id_list.append(bus_id)
            except ValueError:
                id_list.append(bus_id) # If it is an "x" just append as is

    print (id_list)
    return id_list



if __name__ == "__main__":
    id_list = parse_input()
    print(matching_offsets(id_list))