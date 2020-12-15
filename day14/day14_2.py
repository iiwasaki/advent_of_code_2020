"""
Parses instructions and outputs the sum of all
values left in the "memory" after it completes.
This is for part 2, where the bitmask alters the
memory address, not the values.
"""

def process_instructions(instruction_list):
    """
    Processes the instructions in the instruction list
    and returns the sum of all values left in the memory.
    """
    memory_dict = {} # Represents the "memory"
    mask = ""
    for instr in instruction_list:
        if instr[0] == "mask":
            mask = instr[1]
        else:
            mem_address = resolve_address(mask, instr[1])
            for addr in mem_address:
                addr = int(addr, 2)
                memory_dict[addr] = instr[2]

    # Calculate sum of all values left in memory
    total_sum = 0
    for key in memory_dict:
        total_sum += memory_dict[key]

    return total_sum

def resolve_address(mask, addr):
    """
    Take in a mask and starting address, and resolve the possible
    addresses that can be reached with the X in the mask representing
    floating.
    """
    addr_list = [""]
    for index in range(len(mask)-1, -1, -1):
        bit = mask[index]
        if bit == "1":
            for a_index, address in enumerate(addr_list):
                address = "1" + address
                addr_list[a_index] = address
        elif bit == "0":
            bin_addr = bin(addr)
            for a_index, address in enumerate(addr_list):
                address = bin_addr[len(bin_addr) - 1] + address
                addr_list[a_index] = address
        else:
            temp_list = []
            for index, address in enumerate(addr_list):
                temp_list.append(address)
                address = "0" + address
                addr_list[index] = address
            for address in temp_list:
                address = "1" + address
                addr_list.append(address)
        addr = addr >> 1

    return addr_list

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