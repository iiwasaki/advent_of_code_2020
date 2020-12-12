"""
Ship class to represent the ferry we are on.
Takes in instructions and keeps track of its position.
"""

class Ship:
    CARDINALS = ["E", "S", "W", "N"]

    def __init__(self, start_face):
        """
        Initializes the ship object.
        start_face must be given in a range of 0-3, 0 being east.
        """
        self.face = start_face
        self.path_dict = {
            "E": 0,
            "S": 0,
            "W": 0,
            "N": 0
        }

    def move(self, action, amount):
        """
        Performs the given action to change either the position
        or the direction by the particular amount
        """
        if action in Ship.CARDINALS:
            self.path_dict[action] += amount
        if action == "F":
            # Head in the direction it is facing
            direction = Ship.CARDINALS[self.face]
            self.path_dict[direction] += amount
        if action == "R":
            shift = amount // 90
            self.face = (self.face + shift) % 4
        if action == "L":
            shift = 4 - ((amount // 90) % 4)
            self.face = (self.face + shift) % 4

    def manhattan_distance(self):
        """
        Calculates the Manhattan distance, the sum of the
        absolute values of its E/W position and the N/S position.
        """
        dist_ns = self.path_dict["N"] - self.path_dict["S"]
        dist_ew = self.path_dict["E"] - self.path_dict["W"]

        return abs(dist_ns) + abs(dist_ew)

def parse_input():
    """
    Parses the input text given for the ship's movement instructions
    """
    command_list = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            command = line[0]
            amount = int(line[1:])
            command_list.append((command, amount))

    return command_list

if __name__ == "__main__":
    cruise_ferry = Ship(0) # Create ship object facing East (0)
    commands = parse_input()
    for command in commands:
        cruise_ferry.move(command[0], command[1])
    print (cruise_ferry.manhattan_distance())
