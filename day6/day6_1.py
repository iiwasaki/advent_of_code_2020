def sum_answers():
    """
    Returns the number of answers that at least someone in the group
    answered "yes" to.
    """
    total = 0
    with open("input.txt", "r") as input_file:
        lines = input_file.read()
        all_answers = lines.split('\n\n')
        for group in all_answers:
            ans_dict = {}
            individual_ans = group.split('\n')
            for line in individual_ans:
                for letter in line:
                    if letter not in ans_dict:
                        ans_dict[letter] = 1
                        total += 1
    return total

if __name__ == "__main__":
    print(sum_answers())