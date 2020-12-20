"""
Takes in a bunch of rules and characters and returns
characters that follow rule 0.
"""

def count_matches(chars, resolved, rule_num):
    """
    Counts how many strings match the rules given in rule # rule_num.
    """
    match = 0
    valid_set = resolved[rule_num]
    for to_check in chars:
        if to_check in valid_set:
            match += 1

    return match

def match_with_loops(chars, resolved):
    """
    Matches to rule 0 with repeats included for rules 8 and 11.
    """
    match = 0
    interval = 8
    for to_check in chars:
        check_start = 0
        check_end = interval
        if len(to_check) < 3*interval:
            continue
        first_frag = to_check[check_start:check_end]
        if not first_frag in resolved[42]:
            continue
        check_end += interval
        check_start += interval
        match_42 = False
        num_42 = 0
        while True:
            frag = to_check[check_start:check_end]
            if frag in resolved[42]:
                num_42 += 1
                match_42 = True
            else:
                check_start += interval
                check_end += interval
                break
            check_start += interval
            check_end += interval
            if check_end >= len(to_check):
                break
        if not match_42:
            continue
        match_31 = False
        num_31 = 0
        while True:
            frag = to_check[check_start:check_end]
            if frag in resolved[31]:
                num_31 += True
                if check_end == len(to_check):
                    match_31 = True
                    break
            else:
                match_31 = False
                break
            check_start += interval
            check_end += interval
            if check_end > len(to_check):
                match_31 = False
                break
        if match_31 and num_31 < num_42:
            match += 1

    return match

def resolve_rules(rules):
    a_index = find_index(rules, "a")
    b_index = find_index(rules, "b")
    rules.pop(a_index)
    rules.pop(b_index)
    resolved = {}
    resolved[a_index] = {"a"}
    resolved[b_index] = {"b"}
    while len(rules) != 0:
        to_remove = []
        for key in rules:
            if is_resolvable(key, rules, resolved):
                to_remove.append(key)
                resolved[key] = set("")
                subrules_list = rules[key]
                for subrules in subrules_list:
                    rules_to_append = []
                    for rule in subrules:
                        rule_set = resolved[int(rule)]
                        if len(rules_to_append) == 0:
                            for item in rule_set:
                                rules_to_append.append(item)
                        else:
                            temp_list = []
                            for item in rule_set:
                                for to_append in rules_to_append:
                                    temp_list.append(to_append + item)
                            rules_to_append = temp_list
                    for to_append in rules_to_append:
                        resolved[key].add(to_append)
        for remove_key in to_remove:
            rules.pop(remove_key)

    return (resolved)


def is_resolvable(key, rules, resolved):
    """
    Returns true if a particular key can be resolved, as in
    all of the subrule parts are already resolved
    """
    subrules_list = rules[key]
    for subrule in subrules_list:
        for rule in subrule:
            if not int(rule) in resolved:
                return False

    return True



def find_index(rules, letter):
    for key in rules:
        if rules[key] == letter:
            return key


def parse_input():
    rules = {}
    chars = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            if line == "\n":
                break
            else:
                index, rule = line[:len(line) - 1].split(": ")
                if rule == "\"b\"" or rule == "\"a\"":
                    rules[int(index)] = rule[1]
                else:
                    rules[int(index)] = []
                    split_pipe = rule.split(" | ")
                    for subrules in split_pipe:
                        subrules = subrules.split(" ")
                        rules[int(index)].append(subrules)
        for line in input_file:
            chars.append(line[:len(line)-1])

    return rules, chars

if __name__ == "__main__":
    rules, chars = parse_input()
    #print (chars[len(chars)-1])
    resolved = resolve_rules(rules)
    match_no_loop = count_matches(chars, resolved, 0)
    match_loops = match_with_loops(chars, resolved)
    print (f"Part 1: No loops = {match_no_loop}")
    print (f"Part 2: With loops = {match_loops + match_no_loop}")