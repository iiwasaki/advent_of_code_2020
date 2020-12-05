import re

def passport_check():
    """
    A much better version of part 1, where this time the fields
    are validated.
    Could definitely be made more efficient if I was better at regex
    and could remove cid or figure out a better way to not count cid
    when determining "How many fields are there?"
    """
    valid_passports = 0
    # Range of valid eye colors
    eyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    match_criteria = "byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:"

    with open('input.txt', 'r') as input_file:
        lines = input_file.read()
        lines = lines.rsplit('\n', 1)
        passports = lines[0].split('\n\n')
        for passport in passports:
            count = re.findall(match_criteria, passport)
            if len(count) < 7:
                continue
            fields = re.split("\s|\n", passport)
            is_valid = 1
            for pairs in fields:
                pair_split = pairs.split(':')
                if not validate_input(pair_split[0], pair_split[1], eyes):
                    is_valid = 0
                    break
            valid_passports += is_valid
        print (valid_passports)

def validate_input(field, value, valid_eyes):
    try:
        if field == "byr":
            return int(value) >= 1920 and int(value) <= 2002
        elif field == "iyr":
            return int(value) >= 2010 and int(value) <= 2020
        elif field == "eyr":
            return int(value) >= 2020 and int(value) <= 2030
        elif field == "hgt":
            height_num = int(value[:len(value)-2])
            height_unit = value[len(value)-2:]
            if height_unit == "cm":
                return height_num >= 150 and height_num <= 193
            elif height_unit == "in":
                return height_num >= 59 and height_num <= 76
        elif field == "hcl":
            if value[0] == "#":
                color_int = int("0x"+value[1:], 16)
                return color_int >= 0 and color_int <= 16777215
        elif field == "ecl":
            return value in valid_eyes
        elif field == "pid":
            if len(value) == 9:
                return int(value) == 0 or int(value)
        elif field == "cid":
            return True
    except:
        pass
    # To reach this false, the field must be invalid (not match above)
    # or the value must be invalid.
    return False

if __name__ == "__main__":
    passport_check()