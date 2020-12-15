"""
Parses instructions and outputs the sum of all
values left in the "memory" after it completes.
"""

def process_instructions(instruction_list):
    """
    Processes the instructions in the instruction list
    and returns the sum of all values left in the memory.
    """
    memory_dict = {} # Represents the "memory"
    and_mask = 0
    or_mask = 0
    for instr in instruction_list:
        if instr[0] == "mask":
            and_mask, or_mask = make_masks(instr[1])
        else:
            mem_value = instr[2] & and_mask
            mem_value = mem_value | or_mask
            memory_dict[instr[1]] = mem_value

    # Calculate sum of all values left in memory
    total_sum = 0
    for key in memory_dict:
        total_sum += memory_dict[key]

    return total_sum

def make_masks(mask):
    """
    Takes in a mask in the form of Xs, 1s, and 0s and
    creates two masks to be and-ed and or-ed. The mask to
    be and-ed is going to be all 1s except for where there
    are 0s, and the mask to be or-ed will be all 0s except
    for where there are 1s.
    """
    and_mask = ""
    or_mask = ""
    for letter in mask:
        if letter == "X":
            and_mask += "1"
            or_mask += "0"
        else:
            and_mask += letter
            or_mask += letter
    and_mask = int(and_mask, 2)
    or_mask = int(or_mask, 2)

    return and_mask, or_mask

def parse_input():
    """
    Parses the input file and returns it in a list
    form, where each entry in the list is a tuple of
    (instruction, mask/memory address, value).
    """
    with open("input.txt", "r") as input_file:
        instruction_list = []
        for line in input_file:
            line = line.rsplit("\n", 1)[0]
            line = line.split(" = ")
            if line[0] == "mask":
                instruction = ("mask", line[1])
            else:
                address = line[0]
                l_brack = address.find("[") + 1
                r_brack = address.find("]")
                address = address[l_brack:r_brack]
                instruction = ("mem", int(address), int(line[1]))
            instruction_list.append(instruction)

    return instruction_list

if __name__ == "__main__":
    instr_list = parse_input()
    print(process_instructions(instr_list))