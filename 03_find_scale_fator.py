# Funtions go here


# number checking function
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
            print('please enter a number ')


# main route here
serving_size = num_check('what is the serving size for the recipe ')
desired_size = num_check('how many serving are needed ')

scale_factor = desired_size / serving_size
print('the scale factor is',scale_factor)
