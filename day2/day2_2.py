def main():
    valid_passwords = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            segments = line.split()
            min_max = segments[0].split('-')
            
            #Adjust for nonzero-indexing  
            ix_one = int(min_max[0]) - 1
            ix_two = int(min_max[1]) - 1
            letter = segments[1].split(":")[0]
            password = segments[2]
            if (password[ix_one] == letter and 
                password[ix_two] == letter):
                continue
            elif (password[ix_one] == letter or
                  password[ix_two] == letter):
                valid_passwords += 1
    print (valid_passwords)

if __name__ == "__main__":
    main()
