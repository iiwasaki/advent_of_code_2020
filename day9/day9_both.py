def first_violation():
    """
    Finds the first instance of a violation of the
    XMAS code.
    """
    previous = [] #Should only hold 25 at max
    with open("input.txt", "r") as input_file:
        xmas_data = input_file.readlines()

        # First process preamble list
        for i in range (0, 25):
            previous.append(int(xmas_data[i]))

        # Now go through and find the first invalid instance
        for i in range (25, len(xmas_data)):
            data_val = int(xmas_data[i])
            is_valid = False
            for first_num in previous:
                diff = data_val - first_num
                if diff in previous and diff != first_num:
                    # Valid number
                    is_valid = True
                    previous.pop(0)
                    previous.append(data_val)
                    break
            if not is_valid:
                return data_val

        # All valid?
        return -1

def find_weakness(invalid_num):
    """
    Finds the "encryption weakness" based off of the first
    invalid number in the list.
    """
    with open ("input.txt", "r") as input_file:
        current_sum = 0
        contiguous_range = []
        for line in input_file:
            int_val = int(line)
            current_sum += int_val
            contiguous_range.append(int_val)
            while current_sum > invalid_num:
                current_sum -= contiguous_range.pop(0)
            if current_sum == invalid_num:
                smallest = min(contiguous_range)
                largest = max(contiguous_range)
                return smallest + largest

    # If we are here, this means that there was either no
    # contiguous list that sums to invalid number, or the
    # algorithm is wrong.
    return -1

if __name__ == "__main__":
    violation = first_violation()
    print(find_weakness(violation))