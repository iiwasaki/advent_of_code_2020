def sum_all_answers():
    """
    Returns the number of answers for which everybody answered yes to.
    """
    total = 0
    with open("input.txt", "r") as input_file:
        lines = input_file.read()
        all_answers = lines.split('\n\n')
        for group in all_answers:
            ans_dict = {}
            number_of_members = 0
            individual_ans = group.split('\n')
            for line in individual_ans:
                if not line:
                    break
                number_of_members += 1
                for letter in line:
                    if letter not in ans_dict:
                        ans_dict[letter] = 1
                    else:
                        ans_dict[letter] += 1
            for key in ans_dict:
                if ans_dict[key] == number_of_members:
                    total += 1
    return total

if __name__ == "__main__":
    print(sum_all_answers())