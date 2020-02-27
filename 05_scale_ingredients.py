# Ingredients List


# Number Checking Function
def num_check(question):
    error = 'please enter a number that is more than zero'
    valid = False
    while not valid:

        response = input(question)
        if response.lower() == 'xxx':
            return 'xxx'
        else:
            try:
                response = float(response)
                if response <= 0:
                    print(error)
                else:
                    return response
            except ValueError:
                print(error)


# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False
    while not valid:

        response = input(question)
        has_errors = ""
        if num_ok != 'yes':
            for letter in response:
                if letter.isdigit():
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


# Main Routine...

# Replace line below with component 3 in due course...
scale_factor = float(input('Scale Factor: '))

# Set up empty ingredient list
ingredients = []

# Loop to ask users to enter an ingredient
stop = ''
while stop != 'xxx':

    amount = num_check("What is the amount for the ingredient? ")

    # If exit code is typed and there are more than 2 ingredients
    # break out of loop
    if amount == 'xxx' and len(ingredients) > 1:
        break
    
    # If exit code is typed and there are less than 2 ingredients, 
    # show error and go back to start of loop
    elif amount =='xxx' and len(ingredients) < 2:
        print('You need at least two ingredients in the list. ',
              'please add more ingredients')
        continue

    # Ask user for ingredient (via no blank funcion)
    get_ingredient = not_blank("Please type in an ingredient name: ",
                                   "this can't be blank",
                                   "yes")
    
    amount = float(amount) * scale_factor
    ingredients.append('{} units {}'.format(amount,get_ingredient))

print('Your ingredient list: ',ingredients)













# Output list
