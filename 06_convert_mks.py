# ask user for amount
# ask user for Unit
# check that unit is in dictionary

# if unit in dictionary, convert to mL

# if no unit given / unit is unknown, leave as is.

unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

amount = eval(input("How much?"))
amount = float(amount)

unit = input("Unit? ")

if unit in unit_central:
    mult_by = unit_central.get(unit)
    amount = amount * mult_by
    print("Amount in ml {}".format(amount))
else:
    print("{} is unchanged".format(amount))