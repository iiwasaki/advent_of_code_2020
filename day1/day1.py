def main(): 
    inputDict = {} 
    with open('input.txt', 'r') as input_file:
        data = input_file.readlines() 
        for line in data:
            input_int = int(line)
            sum_to_2020 = 2020 - input_int
            if sum_to_2020 in inputDict:
                print (sum_to_2020 * input_int)
            else:
                inputDict[input_int] = 1
                
if __name__ == "__main__":
    main()