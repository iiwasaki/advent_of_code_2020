"""
Given a lit of starting numbers, play the
elf memory game until specified turn and return the number spoken.
This is very brute-forcey right now. Part 2's challenge works
on this as well, but I am sure there is a mathematically faster
way for this to be done.
"""

def play_game(starting_nums, turn_limit):
    """
    Plays the game. Keeps track of a number spoken and the
    turns it was spoken at in a dictionary to determine what
    to speak next.
    """
    turn = 1
    nums_dict = {}
    nums_dict[0] = []
    last_num = -1
    for number in starting_nums:
        if number in nums_dict:
            nums_dict[number].append(turn)
        else:
            nums_dict[number] = [turn]
        turn += 1
        last_num = number
    while turn <= turn_limit:
        prev_list = nums_dict[last_num]
        list_len = len(prev_list)
        if list_len < 2:
            nums_dict[0].append(turn)
            if len(nums_dict[0]) > 2:
                nums_dict[0].pop(0)
            last_num = 0
        else:
            new_num = prev_list[list_len - 1] - prev_list[list_len - 2]
            if new_num in nums_dict:
                nums_dict[new_num].append(turn)
                if len(nums_dict[new_num]) > 2:
                    nums_dict[new_num].pop(0)
            else:
                nums_dict[new_num] = [turn]
            last_num = new_num
        turn += 1
    return last_num

if __name__ == "__main__":
    start_list = [0, 20, 7, 16, 1, 18, 15]
    print(play_game(start_list, 30000000))
