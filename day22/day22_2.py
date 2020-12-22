"""
Play a game of "Recursive Combat" where the rules are
slightly different (Check Day 22, Part 2 of AoC for exact
rule details; the details are far too complex to write here.)
"""

def process_input():
    """
    Read input file in the format:
    Player 1 Deck:
    #
    #
    #

    Player 2 Deck:
    #
    #
    #

    and return as two different lists, each list representing a deck.
    """
    player1_deck = []
    player2_deck = []
    with open("input.txt", "r") as input_file:
        line = input_file.readline() # Read the player 1 part
        for line in input_file:
            if line == "\n":
                break # This splits player 1 and player 2
            line = int(line)
            player1_deck.append(line)
        line = input_file.readline()
        for line in input_file:
            line = int(line)
            player2_deck.append(line)

    return player1_deck, player2_deck

def recursive_combat (p1_deck, p2_deck):
    """
    Simulates a game of recursive combat.
    """
    round = 1
    configs_played = set()
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        current_config = (deck_to_string(p1_deck) + "|" + deck_to_string(p2_deck))
        if current_config in configs_played:
            return "player1"
        configs_played.add(current_config)
        #print(f"-- Round {round} --")
        #print(f"P1's deck: {p1_deck}")
        #print(f"P2's deck: {p2_deck}")
        p1_card = p1_deck.pop(0)
        #print(f"P1 plays: {p1_card}")
        p2_card = p2_deck.pop(0)
        #print(f"P2 plays: {p2_card}")
        if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
            # Go into the sub-game
            p1_copy = p1_deck.copy()[:p1_card]
            p2_copy = p2_deck.copy()[:p2_card]
            winner = recursive_combat(p1_copy, p2_copy)
            if winner == "player1":
                #print("Player 1 wins the round!")
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)
            else:
                 # Player 2 is the winner
                #print("Player 2 wins the round!")
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)
        else:
            # Play a normal game
            if p1_card > p2_card:
                # Player 1 is the winner
                #print("Player 1 wins the round!")
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)
            else:
                # Player 2 is the winner
                #print("Player 2 wins the round!")
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)
        round += 1
    #print()
    #print("== Post-game results ==")
    #print(f"Player 1's deck: {p1_deck}")
    #print(f"Player 2's deck: {p2_deck}")
    if len(p1_deck) > 0:
        # P1 won
        return "player1"
    # Otherwise P2 wins
    return "player2"

def calculate_score(deck):
    """
    Calculates the score of the winning deck (the one that has
    values left in it).
    """
    multiplier = 1
    score = 0
    for index in range (len(deck)-1, -1, -1):
        score += (multiplier * deck[index])
        multiplier += 1

    return score

def deck_to_string(deck):
    """
    Stringifies a deck.
    """
    string = ""
    for card in deck:
        string = string + str(card)

    return string


if __name__ == "__main__":
    p1_deck, p2_deck = process_input()
    winner = recursive_combat (p1_deck, p2_deck)
    score = -1
    print(p1_deck)
    print(p2_deck)
    if winner == "player1":
        print("Winner: Player 1")
        score = calculate_score(p1_deck)
    else:
        print("Winner: Player 2")
        score = calculate_score(p2_deck)
    print(f"The winner's score was {score}")