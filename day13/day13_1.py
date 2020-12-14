"""
Finds the first available bus to take based on the timetable and
returns the product of the Bus ID and how long you have to wait.
"""

def calculate_leave(time, id_list):
    """
    Figures out the first available time to leave based on Bus ID list.
    Returns the product of Bus ID and how long you have to wait.
    """
    earliest_bus = -1
    shortest_wait = time # Just set it to be some arbitrary high number
    for bus in id_list:
        wait_time = bus - (time % bus)
        if wait_time < shortest_wait:
            shortest_wait = wait_time
            earliest_bus = bus

    return earliest_bus * shortest_wait


def parse_input():
    """
    Parses the input file and returns a tuple in the format:
    (first_available_minute, [list_of_bus_IDs])
    """
    with open("input.txt", "r") as input_file:
        id_list = []
        line = input_file.readline()
        first_available = int(line)
        line = input_file.readline().split(',')
        for bus_id in line:
            try:
                bus_id = int(bus_id)
                id_list.append(bus_id)
            except ValueError:
                pass # Do nothing if it is an "x" or some other non-integer
    return (first_available, id_list)

if __name__ == "__main__":
    time, id_list = parse_input()
    print (calculate_leave(time, id_list))
