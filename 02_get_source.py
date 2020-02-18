# get recipe name and check if it's not blank


# check if the name is not blank
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False
    while not valid:

        response = input(question)
        has_errors = ""
        if num_ok != 'yes':
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = 'yes'
                    break

        if response == "":
            print(error_msg)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# ask user for recipe name
source = not_blank("where is the recipe from? ",
                   "the source can't be blank, ",
                   "yes")


print("Source: {}".format(source))










