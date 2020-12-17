"""
Finds the numbers that are invalid (do not meet any of the)
classification requirements and sums them all together.
"""

def six_departure_fields(field_dict, formatted_dict, tickets):
    """
    Taking in both dictionaries (could probably be made more efficient
    with another helper method that just makes a list of all of the
    fields), return the indices of all of the fields that start
    with the word "departure."
    """
    all_fields = set()
    for key in field_dict:
        all_fields.add(key)

    # This field_list will keep track of which index is what field.
    # It will start off with every index having every field be potentially
    # valid. Each index's set will shrink as we eliminate invalid ones.
    field_list = []
    for _ in range (0, len(all_fields)):
        field_list.append(all_fields.copy())

    for ticket in tickets:
        for index, ticket_num in enumerate(ticket):
            ticket_num = int(ticket_num)
            possible_values = set(formatted_dict[ticket_num])
            index_possible = possible_values.intersection(field_list[index])
            field_list[index] = index_possible

    # Go through the field list, finding indices that have just one item
    # which means that is the only place where that can be valid. Remove
    # that from the other lists, and repeat the process.
    field_dict = finalize_list(field_list)

    six_fields = []
    for key in field_dict:
        if field_dict[key].find("departure") != -1:
            six_fields.append(key)

    return six_fields

def finalize_list(field_list):
    """
    Take in a list of lists and find indices that have just one item
    which means that is the only place where that can be valid. Remove
    that from the other lists, and repeat the process.
    Returns a dictionary that has {key: index, value: field}
    """
    return_dict = {}
    num_fields = len(field_list)
    while True:
        to_remove = []
        for index, fields in enumerate(field_list):
            if len(fields) == 1:
                field = fields.pop()
                return_dict[index] = field
                to_remove.append(field)
        for fields in field_list:
            for remove_field in to_remove:
                if remove_field in fields:
                    fields.remove(remove_field)
        if len(return_dict.keys()) == num_fields:
            break

    return return_dict

def find_errors(formatted_dict, tickets):
    """
    Takes in a class dictionary as formatted below and
    a list of the nearby tickets, and returns the sum of all
    of the invalid numbers. Also returns a new list of tickets
    with invalid tickets eliminated.
    """
    invalid_sum = 0
    valid_tickets = []
    for ticket in tickets:
        valid = True
        for num in ticket:
            num = int(num)
            if not num in formatted_dict:
                invalid_sum += num
                valid = False
        if valid:
            valid_tickets.append(ticket)

    return invalid_sum, valid_tickets

def format_dict(field_dict):
    """
    Takes in a dictionary of just {key: field/class, value:
                        tuple(range1, range2)}
    and turns it into a dictionary of format:
        {key: number,
         value: list of potential fields this number could be}
    """
    formatted_dict = {}
    for key in field_dict:
        range1 = field_dict[key][0].split("-")
        range2 = field_dict[key][1].split("-")
        r1_low = int(range1[0])
        r1_high = int(range1[1])
        r2_low = int(range2[0])
        r2_high = int(range2[1])
        for index in range(r1_low, r1_high + 1):
            if index in formatted_dict:
                formatted_dict[index].append(key)
            else:
                formatted_dict[index] = [key]
        for index in range(r2_low, r2_high + 1):
            if index in formatted_dict:
                formatted_dict[index].append(key)
            else:
                formatted_dict[index] = [key]

    return formatted_dict

def parse_input(num_classes):
    """
    Parses user input and returns it in the form of:
    field_dict is a dictionary of: {key: field/class, value:
            tuple(range1, range2)}
    my_ticket = list of numbers on each field (as str, not int)
    nearby_tickets = list of list of numbers of each field (as str)
    """
    field_dict = {}
    my_ticket = []
    nearby_tickets = []
    with open("input.txt", "r") as input_file:
        for _ in range(0, num_classes):
            line = input_file.readline()
            line = line.split(": ")
            field = line[0]
            ranges = line[1].split(" or ")
            field_dict[field] = (ranges[0], ranges[1])

        line = input_file.readline() # Read extra newline only
        line = input_file.readline() # Read extra "your ticket:"

        my_ticket = input_file.readline().split(",")

        line = input_file.readline() # Read extra newline
        line = input_file.readline() # Read extra "nearby tickets:"

        for line in input_file:
            nearby_tickets.append(line.split(","))

    return field_dict, my_ticket, nearby_tickets

if __name__ == "__main__":
    classes = 20  # How many different fields there are
    field_dict, my_ticket, nearby_tickets = parse_input(classes)
    formatted = format_dict(field_dict)
    invalid_count, valid_tickets = find_errors(formatted, nearby_tickets)
    six = six_departure_fields(field_dict, formatted, valid_tickets)
    product = 1
    for index in six:
        product *= int(my_ticket[index])
    print (invalid_count)
    print (product)