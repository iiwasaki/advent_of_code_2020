def main():
    place_in_line = 0
    current_line = 0
    tree_count = 0
    with open('input.txt', 'r') as input_file: 
        lines = input_file.readlines()
        number_of_lines = len(lines)
        # To remove the newline char, remove 1
        line_length = len(lines[0]) - 1
        while True:
            place_in_line = (place_in_line + 3) % line_length
            current_line = (current_line + 1) 
            if current_line >= number_of_lines: 
                break
            if lines[current_line][place_in_line] == "#":
                tree_count = tree_count + 1
    print (tree_count)

if __name__ == "__main__":
    main() 