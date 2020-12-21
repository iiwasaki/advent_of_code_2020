"""
Identifies allergens in the menu.
Finds the ingredients that cannot possibly have any allergens.
"""

def resolve_allergens(al_dict):
    """
    Figures out what ingredients have what allergens. Returns
    in a dictionary with format {allergen: ingredient}
    """
    known_ings = set()
    resolved_dict = {}
    while len(known_ings) < len(al_dict):
        for allergen in al_dict:
            if allergen in known_ings:
                continue
            common_ings = set.intersection(*al_dict[allergen])
            common_ings = common_ings.difference(known_ings)
            if len(common_ings) == 1:
                resolved_dict[allergen] = common_ings.pop()
                known_ings.add(resolved_dict[allergen])
                print (f"Allergen {allergen} is in {resolved_dict[allergen]}")

    return resolved_dict

def count_safe(all_ings, al_dict):
    """
    Returns the number of times that an ingredient that has no allergens
    appears in a list of ingredients.
    """
    safe = 0
    ings_with_allergens = al_dict.values()
    ings_with_allergens = set(ings_with_allergens)
    for ing_list in all_ings:
        for ingredient in ing_list:
            if not ingredient in ings_with_allergens:
                safe += 1

    return safe

def parse_input():
    """
    Parses user input and returns a list of ingredients and
    a dictionary containing allergens and ingredients that may have
    those allergens. That dictionary must be resolved (above).
    """
    allergy_dict = {}
    ing_list = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.split(" (contains ")
            ingredients = line[0].split()
            ing_list.append(ingredients)
            ingredients = set(ingredients)
            allergens = line[1].strip(")\n").split(", ")
            for allergen in allergens:
                if allergen in allergy_dict:
                    allergy_dict[allergen].append(ingredients)
                else:
                    allergy_dict[allergen] = [ingredients]

    return ing_list, allergy_dict

def dangerous_list(resolved_dict):
    """
    Takes in a list of allergens, and returns a string of ingredients
    with allergens sorted alphabetically by allergen.
    """
    dangerous = ""
    allergens = [*resolved_dict]
    allergens.sort()
    for allergen in allergens:
        ingredient = resolved_dict[allergen]
        dangerous = dangerous + ingredient + ","

    return dangerous[:len(dangerous)-1]

if __name__ == "__main__":
    ingredients, allergen_dict = parse_input()
    resolved_dict = resolve_allergens(allergen_dict)
    num_safe = count_safe(ingredients, resolved_dict)
    print(f"There are {num_safe} occurrences of safe ingredients.")
    dangerous_ings = dangerous_list(resolved_dict)
    print(f"The dangerous ingredient list is {dangerous_ings}")
