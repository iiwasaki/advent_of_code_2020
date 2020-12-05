import re

def main():
    """
    Counts the number of valid passports in the input text.
    Definitely not the most robust answer, as it ignores
    invalid fields (if any) and also ignores invalid values to
    necessary fiends (e.g. a "height" of "abcdef")
    """
    valid_passports = 0
    with open('input.txt', 'r') as input_file:
        match_criteria = "byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:"
        lines = input_file.read()
        passports = lines.split('\n\n')
        for passport in passports:
            fields = re.findall(match_criteria, passport)
            print (fields)
            if len(fields) == 7:
                valid_passports += 1
    print (valid_passports)

if __name__ == "__main__":
    main()
