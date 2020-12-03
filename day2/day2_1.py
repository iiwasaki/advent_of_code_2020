def main():
    valid_passwords = 0
    with open('input.txt', 'r') as input_file:
        data = input_file.readlines()
        for line in data:
            segments = line.split()
            min_max = segments[0].split('-')
            letter = segments[1].split(":")[0]
            password = segments[2]
            count = 0 
            for pass_char in password:
                if pass_char == letter:
                    count += 1
                    if count > int(min_max[1]):
                        break 
            if count >= int(min_max[0]) and count <= int(min_max[1]):
                valid_passwords += 1
    print (valid_passwords)

if __name__ == "__main__":
    main()