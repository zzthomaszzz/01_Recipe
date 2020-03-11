# ask user for amount
# ask user for Unit
# check that unit is in dictionary

# if unit in dictionary, convert to mL

# if no unit given / unit is unknown, leave as is.


# function here
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by * conversion_factor

    return how_much



def unit_checker():
    unit_tocheck = input("Unit? ")

    teaspoon = ["tsp","teaspoon","t"]
    tablespoon = ["tbs","tablespoon","T","tbsp"]
    cup = ["c","cup"]
    ounce = ["oz","fluid","ounce","fl-pt"]
    pint = ["p","qt","fl","gt","pint"]
    quart = ["q","qt","quart","fl-qt"]
    pound = ["lb","#","pound"]

    if unit_tocheck == "":
        print('you chose {}'.format(unit_tocheck))
        return unit_tocheck
    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck == 'C' or unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in pound:
        return "pound"
    else:
        pass

unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

keep_going = ""
while keep_going == "":
    amount = eval(input("how much? "))
    amount = float(amount)

    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)


    keep_going = input("<enter> or q")






