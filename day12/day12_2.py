"""
Ship class to represent the ferry we are on.
Takes in instructions and keeps track of both the waypoint
and the ship's position.
"""

class Ship:
    def __init__(self):
        """
        Initializes the ship object.
        start_face must be given in a range of 0-3, 0 being east.
        North/East are +, South/West are - in its respective directions.
        """
        self.ship_ns = 0
        self.ship_ew = 0

        # Hardcoding waypoint start, but... oh well?
        self.waypoint_ns = 1
        self.waypoint_ew = 10

    def move(self, action, amount):
        """
        Performs the given action to change either the position
        or the direction by the particular amount. Adjusts waypoint
        as necessary.
        """
        if action == "E":
            self.waypoint_ew += amount
            return
        if action == "W":
            self.waypoint_ew -= amount
            return
        if action == "N":
            self.waypoint_ns += amount
            return
        if action == "S":
            self.waypoint_ns -= amount
            return
        if action == "F":
            # Head in the direction it is facing
            self.ship_ew = self.ship_ew + (amount * self.waypoint_ew)
            self.ship_ns = self.ship_ns + (amount * self.waypoint_ns)
            return
        if action == "R" or action == "L":
            shift = amount // 90
            if action == "L":
                shift = 4 - (shift % 4) # Translate it all to a right shift
            for _ in range (0, shift):
                temp_ew = self.waypoint_ew
                self.waypoint_ew = self.waypoint_ns
                self.waypoint_ns = temp_ew * -1

    def manhattan_distance(self):
        """
        Calculates the Manhattan distance, the sum of the
        absolute values of its E/W position and the N/S position.
        """

        return abs(self.ship_ew) + abs(self.ship_ns)

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
    cruise_ferry = Ship() # Create ship object
    commands = parse_input()
    for command in commands:
        cruise_ferry.move(command[0], command[1])
    print (cruise_ferry.manhattan_distance())
