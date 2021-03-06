"""
Processes math given the conditions that additions are
evaluated before multiplication in the order of operations.
Parentheses still get preference.
"""

def formula_sums():
    total_sum = 0
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = process_parens(line)
            total_sum += do_math(line)

    return total_sum

def process_parens(line):
    """
    Take a formula line and process parentheses first.
    """
    while line.rfind("(") != -1:
        l_paren_ix = line.rfind("(")
        r_paren_ix = line.find(")", l_paren_ix)
        result = do_math(line[l_paren_ix + 1:r_paren_ix])
        line = line[:l_paren_ix] + str(result) + line[r_paren_ix+1:]

    return line

def do_math(func):
    """
    Given a certain function consisting of numbers, *, and +,
    calculate what the result will be if addition has higher priority
    than multiplication.
    Assumes that the functions are all in valid format, as in
    it follows the number operator number format legally.
    """
    splits = func.split(" ")
    operator_next = False
    op_num = 0
    operator = ""
    mult_list = []
    for entry in splits:
        if operator_next:
            operator = entry
            operator_next = False
        else:
            if operator == "*":
                mult_list.append(op_num)
                op_num = int(entry)
            elif operator == "+":
                op_num += int(entry)
            else:
                op_num = int(entry)
            operator_next = True
    for number in mult_list:
        op_num *= number

    return op_num

if __name__ == "__main__":
    sums = formula_sums()
    print (sums)