"""
Takes in a bunch of rules and characters and returns
characters that follow rule 0.
"""

def resolve_rules(rules):
    a_index = find_index(rules, "a")
    b_index = find_index(rules, "b")
    print (a_index)
    print (b_index)

def find_index(rules, letter):
    for key in rules:
        if rules[key] == letter:
            return key


def parse_input():
    rules = {}
    chars = []
    with open("test.txt", "r") as input_file:
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
            chars.append(line)

    return rules, chars

if __name__ == "__main__":
    rules, chars = parse_input()
    #print (chars[len(chars)-1])
    resolve_rules(rules)