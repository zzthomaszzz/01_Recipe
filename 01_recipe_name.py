# get recipe name and check if it's not blank


#string

error = "your recipe can not have number in it"





# check if the name is not blank
def not_blank(question):
    valid = False
    while not valid:

        response = input(question)
        has_errors = ""

        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"

                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response







# ask user for recipe name

recipe_name = not_blank(" what would you like to make? ")

print("you are making {}".format(recipe_name))










