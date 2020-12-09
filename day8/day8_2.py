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

def get_jumps_nops(instruction_list):
    """
    Goes through the instructions given in the
    instruction_list until an infinite loop is detected.
    Keeps track of all of the jumps and no-ops in the order
    that they are executed and returns that list.
    """
    done_instructions = []
    jumps_and_nops = []
    inst_num = 0
    while True:
        if inst_num in done_instructions:
            break
        if instruction_list[inst_num][0] == "nop":
            jumps_and_nops.append(inst_num)
            pass
        elif instruction_list[inst_num][0] == "acc":
            pass
        elif instruction_list[inst_num][0] == "jmp":
            done_instructions.append(inst_num)
            jump_amount = instruction_list[inst_num][1]
            jumps_and_nops.append(inst_num)
            inst_num += jump_amount
            continue
        else:
            return -1 #Error in instruction list
        done_instructions.append(inst_num)
        inst_num += 1

    return jumps_and_nops

def find_inf_loop(instruction_list, jumpnop_list):
    """
    Using the list of jumps and nops,
    attempts to find the cause of the infinite loop and fix it.
    This is pretty brute force.. I want to see a better solution.
    """
    # First, set up all of the variables needed to keep track
    done_instructions = []
    inst_num = 0
    accumulator = 0

    # When to stop
    final_inst = len(instruction_list)

    # Makes the first attempt to change an instruction. Assumes
    # that jumpnop_list is nonempty.
    modified_instructions = instruction_list

    # Do a pop() here so that we start from the last jump/nops done
    # instead of the first. Improves the brute forcing a little bit.
    first_change = jumpnop_list.pop()
    amount = modified_instructions[first_change][1]

    # Do the switch between nop and jump
    if modified_instructions[first_change][0] == "nop":
        modified_instructions[first_change] = ("jmp", amount)
    else:
        modified_instructions[first_change] = ("nop", amount)

    while True:
        # We have gone beyond the final instruction line
        if inst_num >= final_inst:
            break
        # We have hit an infinite loop again
        if inst_num in done_instructions:
            # Try again with next jump switched
            # Reset all the numbers so that we can try from the start
            # Reset modified instructions as well.
            modified_instructions = instruction_list
            inst_num = 0
            accumulator = 0
            done_instructions = []

            # We have failed, no more corrections to make!
            if len(jumpnop_list) == 0:
                return -1

            # Do the switch as before
            to_change = jumpnop_list.pop()
            amount = modified_instructions[to_change][1]
            if modified_instructions[to_change][0] == "nop":
                modified_instructions[to_change] = ("jmp", amount)
            else:
                modified_instructions[to_change] = ("nop", amount)
            continue
        if modified_instructions[inst_num][0] == "nop":
            pass
        elif modified_instructions[inst_num][0] == "acc":
            accumulator += instruction_list[inst_num][1]
        elif modified_instructions[inst_num][0] == "jmp":
            done_instructions.append(inst_num)
            jump_amount = instruction_list[inst_num][1]
            inst_num += jump_amount
            continue
        else:
            return -1 #Error in instruction list
        done_instructions.append(inst_num)
        inst_num += 1

    #If we are here, then we have broken the infinite loop!
    return accumulator

if __name__ == "__main__":
    instruction_list = parse_input()
    jumpnop_list = get_jumps_nops(instruction_list)
    print (find_inf_loop(instruction_list, jumpnop_list))