def main():
    input_dict = {}
    single_values = []
    with open('input.txt') as input_file:
        data = input_file.readlines()
        for line in data:
            input_int = int(line)
            sum_to_2020 = 2020 - input_int
            if sum_to_2020 in input_dict:
                val1 = input_dict[sum_to_2020][0]
                val2 = input_dict[sum_to_2020][1]
                print(input_int * val1 * val2)
            else:
                for seen_number in single_values: 
                    intermediate_sum = seen_number + input_int
                    input_dict[intermediate_sum] = [seen_number, input_int]
                single_values.append(input_int)
if __name__ == "__main__":
    main()