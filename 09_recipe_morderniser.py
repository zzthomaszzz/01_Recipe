# modules to be used
import csv

# ***** Functions ******


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

# ***** Main routine ******


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


# Loop for each ingredients...


# Get ingredient amount
# get ingredient name
# Get unit
# Convert unit to ml
# Convert from ml to g
# Put updated ingredient in list

# Output ingredient list
