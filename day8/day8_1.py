def parse_input():
    """
    Parses the input text and returns a more iterable
    list of instructions in a list. Each list entry
    is a tuple in the form of ("opcode", number).
    This does not do any error checking, so it is
    very dependent on the precondition that the input text
    is formatted as "opcode +/-{int}"
    """
    instruction_list = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.split()
            instr_tuple = (line[0], int(line[1]))
            instruction_list.append(instr_tuple)
    return instruction_list

def find_inf_loop(instruction_list):
    """
    Goes through the instructions given in the
    instruction_list until an infinite loop is detected,
    and returns the accumulator value right beforehand.
    """
    done_instructions = []
    accumulator = 0
    inst_num = 0
    while True:
        if inst_num in done_instructions:
            break
        if instruction_list[inst_num][0] == "nop":
            pass
        elif instruction_list[inst_num][0] == "acc":
            accumulator += instruction_list[inst_num][1]
        elif instruction_list[inst_num][0] == "jmp":
            done_instructions.append(inst_num)
            inst_num += instruction_list[inst_num][1]
            continue
        else:
            return -1 #Error in instruction list
        done_instructions.append(inst_num)
        inst_num += 1

    return accumulator


if __name__ == "__main__":
    instruction_list = parse_input()
    print (find_inf_loop(instruction_list))