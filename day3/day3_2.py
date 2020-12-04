def count_trees(num_right, num_down):
    """
    Returns how many trees ("#") you will encounter by
    moving to the right num_right slots and down num_down 
    slots. 
    """
    place_in_line = 0
    current_line = 0
    tree_count = 0
    with open('input.txt', 'r') as input_file: 
        lines = input_file.readlines()
        number_of_lines = len(lines)
        # To remove the newline char, remove 1
        line_length = len(lines[0]) - 1
        while True:
            place_in_line = (place_in_line + num_right) % line_length
            current_line = (current_line + num_down) 
            if current_line >= number_of_lines: 
                break
            if lines[current_line][place_in_line] == "#":
                tree_count = tree_count + 1

    return tree_count

if __name__ == "__main__":
    trees_1_1 = count_trees(1, 1)
    trees_3_1 = count_trees(3, 1)
    trees_5_1 = count_trees(5, 1)
    trees_7_1 = count_trees(7, 1)
    trees_1_2 = count_trees(1, 2)
    print (trees_1_1 * trees_3_1 * trees_5_1 * trees_7_1 * trees_1_2)