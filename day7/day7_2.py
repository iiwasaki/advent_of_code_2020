def valid_bags(bag_dict):
    """
    Counts how many bags it would take in total that
    one shiny gold bag would take.
    """
    count = 0
    my_bag = [(1, "shiny gold")]
    while (len(my_bag) > 0):
        multiplier, bag_type = my_bag.pop()
        for bag_contents in bag_dict[bag_type]:
            to_add = multiplier * bag_contents[0]
            count += to_add
            my_bag.append((to_add, bag_contents[1]))
    print (count)


def parse_rules():
    """
    Parses an input file and returns a dictionary that represents
    the bag rules.
    """
    bag_dict = {}
    with open("input.txt", "r") as input_file:
        for line in input_file:
            rule_bag, bag_list = line.split(" contain ",1)
            rule_bag = rule_bag.split(" bags",1)[0]
            bag_dict[rule_bag] = []
            #Get rid of all the commas
            bag_list = bag_list.replace(",","")
            bag_list = bag_list.split(" ")
            for x in range (0, len(bag_list), 4):
                if bag_list[x] == "no":
                    continue
                num_of_bags = int(bag_list[x])
                bag_type = bag_list[x+1] + " " + bag_list[x+2]
                bag_tuple = (num_of_bags, bag_type)
                bag_dict[rule_bag].append(bag_tuple)
    return bag_dict

if __name__ == "__main__":
    bag_dict = parse_rules()
    valid_bags(bag_dict)