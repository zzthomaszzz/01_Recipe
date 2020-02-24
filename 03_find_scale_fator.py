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
dodgy_sf ='yes'
while dodgy_sf == 'yes':
    serving_size = num_check('what is the serving size for the recipe ')
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



print('the scale factor is',scale_factor)
