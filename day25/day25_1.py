"""
The final puzzle of Advent of Code 2020!
It was fun (at times) and frustrating (at times) but very much
worth it!

This attempts to "break" the encryption system for the hotel room door
by brute forcing the secret loop size that produces the public keys.
"""

def loop_num(card_pub, door_pub):
    """
    Given a set of public keys, tries to figure out at least
    one of the loop numbers.
    """
    value = 1
    subject = 7
    loop_count = 1
    while True:
        value = value * subject
        value = value % 20201227
        if value == card_pub or value == door_pub:
            break
        loop_count += 1
    if value == card_pub:
        return ("card", loop_count)

    return ("door", loop_count)

def transform_num(subject, loop_count):
    """
    Run the number transform function for a loop_count
    number of times.
    """
    value = 1
    for _ in range (0, loop_count):
        value = value * subject
        value = value % 20201227

    return value


def parse_input():
    """
    Parse the input file for the two public key values.
    Assumes the first one is the card, second one is the door.
    """
    public_keys = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            public_keys.append(int(line))

    return tuple(public_keys)
if __name__ == "__main__":
    pub_keys = parse_input()
    location, loop = loop_num(pub_keys[0], pub_keys[1])
    enc_key = -1
    if location == "card":
        enc_key = transform_num(pub_keys[1], loop)
    else:
        enc_key = transform_num(pub_keys[0], loop)
    print (f"The encryption key is {enc_key}")