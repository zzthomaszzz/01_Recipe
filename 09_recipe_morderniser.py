# modules to be used
import csv
import re

# ***** Functions ******
def get_all_ingredients():
    all_ingredients = []

    stop = ''
    print("Please enter ingredients one line at a time. Press 'xxx' to when"
          "you are done.")
    while stop != "xxx":

        # Ask user for ingredient (via not blank function)
        get_recipe_line = not_blank("recipe line: ",
                                    "This can;t be blank",
                                    "yes")

        # Stop looping if exit code is typed and there are more than 2 ingredients...
        if get_recipe_line.lower() == "xxx" and len(all_ingredients) > 1:
            break

        elif get_recipe_line.lower() == "xxx" and len(all_ingredients) < 2:
            print("You need atleast two ingredients in the list. "
                  "Please add more ingredients.")
        else:
            all_ingredients.append(get_recipe_line)

        return all_ingredients







def not_blank(question, error_msg, num_ok):

    error = error_msg
    response = input(question)
    has_errors = ''
    if num_ok != "yes":
        for letter in response:
            if letter.isdigit() == True:
                has_errors = 'yes'
                break
    if response == "":
        print(error)
        not_blank(question,error_msg,num_ok)
    elif has_errors != '':
        print(error)
        not_blank(question, error_msg, num_ok)
    else:
        return response

def num_check(question):
    error = 'please enter a number that is more than zero'
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print('please enter a number that is more than zero ')

def get_sf():
    serving_size = num_check('what is the serving size for the recipe ')

    # Main routine goes here
    dodgy_sf = 'yes'
    while dodgy_sf == 'yes':

        desired_size = num_check('how many serving are needed ')
        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: this scale factor is very small "
                             "and you might struggle to accurately weigh"
                             "the ingredients. \n"
                             "do you want to change your serving size? (type 'yes' to change"
                             "your desired serving size )").lower()
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might"
                             "have issues with mixing bowl space / oven space. \n"
                             "Do you want to change your serving size? (type 'yes' to change"
                             "your desired serving size) ").lower()
        else:
            dodgy_sf = 'no'
    return scale_factor


# set up Dictionaries


# set up list to hold 'modernised' ingredients


# Ask user for recipe name and check its not blank
source = not_blank("what is the recipe name? ",
                   "The recipe name can't be blank and can't contain numbers,",
                   "no")

# Ask user where the recipe is originally from (numbers OK)
source = not_blank("where is the recipe from? ",
                   "the source can't be blank, ",
                   "yes")


# Get serving seizes and scale factor
scale_factor = get_sf()



# Get amounts, units and ingredients from user...
full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient...
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # get amount

    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a sign + sign...
        amount = mixed_num.replace(" ","+")
        # Change the string into a decimal
        amount = eval(amount)
        print(amount)

        # Get unit and ingredient...
        compile_regex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip() # remove extra white space from unit
    else:
        get_amount = recipe_line.split(" ", 1) # split line at first space

        try:
            amount = eval(get_amount[0])  # convert amount to float if possible
        except NameError:
            amount = get_amount[0]
            convert = 'no'

        unit_ingredient = get_amount[1]

    # Get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)  # splits text at first space

    unit = get_unit[0]
    # convert into ml
    ingredient = get_unit[1]
    #convert into g

    print("{} {}")








# Output ingredient list