"""
Crab Cups but with 1 million entries and 10 million moves.
Oh boy...
"""
def parse_input(in_string):
    """
    Takes in input string and returns it in list form of integers.
    """
    integer_list = []
    max_num = -1
    for char in in_string:
        integer_list.append(int(char))
        max_num = max(max_num, int(char))
    for num in range (max_num + 1, 1000001):
        integer_list.append(num)

    return integer_list

def crab_cups(cups, round_lim):
    """
    Given a list of integers as cup labels, play Crab Cups for
    x number of rounds, where x is the supplied round limit.
    """
    tuple_set = set()
    current = 0
    for round in range (1, round_lim + 1):
        #print(f"-- Move {round} --")
        #print(f"Cups: {cups}")
        current_val = cups[current]
        #print(f"Current cup: {current_val}")
        cw_one = cups.pop(clockwise_index(cups, cups.index(current_val), 1))
        cw_two = cups.pop(clockwise_index(cups, cups.index(current_val), 1))
        cw_three = cups.pop(clockwise_index(cups, cups.index(current_val), 1))
        #print (f"Pick up: {cw_one}, {cw_two}, {cw_three}")
        destination = find_destination(cups, current_val)
        #print (f"Destination: {cups[destination]}\n")
        cups.insert(destination + 1, cw_one)
        cups.insert(destination + 2, cw_two)
        cups.insert(destination + 3, cw_three)
        current = clockwise_index(cups, cups.index(current_val), 1)
        cup_tup = tuple(cups)
        if cup_tup in tuple_set:
            print ("Repeat found!")
        tuple_set.add(cup_tup)

    return cups

def prep_return(cups):
    """
    Given a list of cups, return a string with all the numbers
    after the "1" in the cups list concatenated together.
    """
    cup_len = len(cups)
    index = (cups.index(1) + 1) % cup_len
    return_str = ""
    for _ in range (0, cup_len - 1):
        return_str += str(cups[index])
        index = (index + 1) % cup_len

    return return_str

def find_destination(cups, current_label):
    """
    Given the index of the current cup, find the destination cup for
    the Crab Game. The destination is the cup that has the current cup
    label minus one, or, if that is not found, the largest cup.
    """
    target = current_label - 1
    largest_num = max(cups)
    smallest_num = min(cups)
    while True:
        if target in cups:
            return cups.index(target)
        target -= 1
        if target < smallest_num:
            target = largest_num

    return -1 # Should never be here


def clockwise_index(cups, current_ix, num_clockwise):
    """
    Given a list of cup labels and a number of times to move clockwise,
    return the index for the cup that is {num_clockwise} to the right of
    the current index.
    """

    return (current_ix + num_clockwise) % len(cups)

if __name__ == "__main__":
    int_list = parse_input("389125467")
    print(len(int_list))
    new_cups = crab_cups(int_list, 10000)
    print(f"Final cups: {len(new_cups)}")
    #to_print = prep_return(new_cups)
    #print(f"Final string: {to_print}")