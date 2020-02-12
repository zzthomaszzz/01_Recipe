# Get recipe name and check if it is not blank

# Not Blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response
# Strings










# Main route goes here

recipe_name = not_blank("what is the recipe name? ")

print ("You are making {}".format(recipe_name))
