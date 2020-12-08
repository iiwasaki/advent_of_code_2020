def valid_bags(bag_dict):
    """
    Counts how many valid bags can hold a shiny gold bag.
    """
    my_bag = ["shiny gold"]
    valid_bag_dict = {}
    while len(my_bag) > 0:
        to_check = my_bag.pop()
        for bag in bag_dict:
            if to_check in bag_dict[bag]:
                my_bag.append(bag)
                valid_bag_dict[bag] = 1
    print (len(valid_bag_dict))

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
                bag_type = bag_list[x+1] + " " + bag_list[x+2]
                bag_dict[rule_bag].append(bag_type)
    return bag_dict

if __name__ == "__main__":
    bag_dict = parse_rules()
    valid_bags(bag_dict)