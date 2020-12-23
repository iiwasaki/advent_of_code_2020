"""
Crab Cups but with 1 million entries and 10 million moves.
Oh boy...
"""
class Cup:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next_cup):
        self.next = next_cup

def parse_input(in_string):
    """
    Takes in input string and creates a cup object for each cup.
    Returns a dictionary that maps a label to a particular cup.
    """
    cup_dict = {}
    max_num = -1
    last_cup = None
    first_cup = None
    for char in in_string:
        cup = Cup(int(char))
        if not first_cup:
            first_cup = cup
        if last_cup:
            last_cup.set_next(cup)
        cup_dict[int(char)] = cup
        last_cup = cup
        max_num = max(max_num, int(char))
    for num in range (max_num + 1, 1000001):
        cup = Cup(num)
        last_cup.set_next(cup)
        cup_dict[num] = cup
        last_cup = cup
    last_cup.set_next(first_cup)

    return cup_dict

def crab_cups(cups, start_label, num_rounds):
    """
    Given a starting cup label, play the cup game for the
    given number of rounds. Now improved to use a linked list with a
    dictionary, not just a list!
    """
    current_cup = cups[start_label]
    for round in range(1, num_rounds + 1):
        #print(f"-- Move {round} --")
        #print_cups(cups, 3)
        pick_ups = (current_cup.next,
                    current_cup.next.next,
                    current_cup.next.next.next)
        destination = find_destination(cups, current_cup, pick_ups)
        #print(f"Get:{pick_ups[0].val}, {pick_ups[1].val}, {pick_ups[2].val}")
        #print(f"Destination: {destination.val}\n")
        current_cup.next = pick_ups[2].next
        pick_ups[2].next = destination.next
        destination.next = pick_ups[0]
        current_cup = current_cup.next

    return cups


def find_destination(cup_dict, current, picked_up):
    """
    Find the "destination" cup given the current cup we are on.
    Destination will be current cup label - 1 unless that cannot be found
    (as in it has been picked up, or does not exist for some other reason).
    Then it will subtract 1 until wrapping around to the top value.
    Returns destination cup.
    """
    target_label = current.val - 1
    while True:
        if target_label in cup_dict:
            target_cup = cup_dict[target_label]
            if not target_cup in picked_up:
                return target_cup
            target_label -= 1
        else:
            target_label = len(cup_dict)


def print_cups(cup_dict, start_label):
    """
    Given a starting label, print out the cups in order starting at the
    start label cup. Assumes start label will always be valid.
    """
    start_cup = cup_dict[start_label]
    cup_str = ""
    for _ in range (0, len(cup_dict)):
        cup_str += str(start_cup.val)
        start_cup = start_cup.next

    print (f"Cups: {cup_str}")

def two_after(cup_dict, start_label):
    """
    Returns the two cups that come after the target cup.
    For the solution, target cup will be "1". Assumes start_label
    will always be valid.
    """
    target_cup = cup_dict[start_label]

    return target_cup.next.val, target_cup.next.next.val

if __name__ == "__main__":
    cup_dict = parse_input("871369452")
    cup_dict = crab_cups(cup_dict, 8, 10000000)
    ans_one, ans_two = two_after(cup_dict, 1)
    print (ans_one)
    print (ans_two)
    print (ans_one * ans_two)