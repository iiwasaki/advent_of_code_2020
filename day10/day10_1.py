def create_joltage_set():
    """
    Parses input to create a set of joltage values so that
    it can be used in later calculations.
    Use a set to keep track of joltages since lookups
    into sets are average-case O(1) and worst-case O(n)
    which is better than performance of lists
    """

    joltage_set = set()
    with open("input.txt", "r") as input_file:
        for line in input_file:
            joltage_set.add(int(line))

    return joltage_set

def find_diffs(joltage_set):
    """
    Takes in an input file of "joltages" and counts
    the number of 1 and 3 difference gaps if all joltages
    were to be used.
    """

    one_diff_count = 0
    three_diff_count = 0
    joltage = 0
    while True:
        if joltage + 1 in joltage_set:
            one_diff_count += 1
            joltage += 1
        elif joltage + 3 in joltage_set:
            three_diff_count += 1
            joltage += 3
        elif joltage + 2 in joltage_set:
            joltage += 2
        else:
            break # Exhausted options, get out of loop

    # Finally, add a value to three_diff_count since the
    # device is a 3 volt difference.
    three_diff_count += 1

    return one_diff_count * three_diff_count

def find_possible_paths(joltage_set):
    """
    An attempt at an efficient general-purpose "all possible paths" count
    algorithm for joltages of 1, 2, 3 vaulue gaps away.
    Inspired by Dijkstra's... in theory.
    """

    # The dictionary that will keep track of the joltage and
    # the corresponding possible # of combinations to that joltage.
    visited_dict = {0: 1}

    # Keeps track of the "frontier" part of Dijkstra's; the set that
    # has not yet had its +1, +2, +3 neighbors processed yet.
    frontier_list = [0]

    while (len(frontier_list) > 0): #As in, while there's stuff to process
        # Pop off the top of the frontier "heap"
        frontier_jolt = frontier_list.pop(0)

        # For each +1, +2, +3 neighbor, process it and adjust
        # the visited_dict and frontier_list as necessary.
        process_neighbor(frontier_jolt,
            frontier_jolt + 1,
            joltage_set,
            visited_dict,
            frontier_list)
        process_neighbor(frontier_jolt,
            frontier_jolt + 2,
            joltage_set,
            visited_dict,
            frontier_list)
        process_neighbor(frontier_jolt,
            frontier_jolt + 3,
            joltage_set,
            visited_dict,
            frontier_list)

    final_value = max(visited_dict.keys())
    total_possible_combinations = visited_dict[final_value]

    return total_possible_combinations

def process_neighbor(curr, next, joltage_set, visited_dict, frontier_list):
    """
    Does the actual "counting" part for this modified Dijkstra's. Changes the
    state of visited_dict and/or frontier_list.
    Only called from find_possible_paths.
    """
    # If this is a possible value in the set
    if next in joltage_set:

        # If the next joltage is already in visited_dict,
        # we basically say there will be one more unique path to it
        # for every path we have to the current joltage.
        if next in visited_dict:
            visited_dict[next] += visited_dict[curr]

        # If the next joltage is not yet in the visited_dict,
        # it's the first time we've gotten to it. Therefore, the
        # number of unique paths to it will be the same as the
        # number of unique paths to the current joltage.
        else:
            visited_dict[next] = visited_dict[curr]
            # Add it to the list of joltages that needs to be processed.
            frontier_list.append(next)

if __name__ == "__main__":
    joltage_set = create_joltage_set()
    print("Multiple of 1 and 3 diff counts: " + str(find_diffs(joltage_set)))
    print("Possible combinations of adapters: " +
           str(find_possible_paths(joltage_set)))