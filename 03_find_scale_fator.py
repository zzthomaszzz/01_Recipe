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
sf_ok ='no'
while sf_ok == 'no':
    serving_size = num_check('what is the serving size for the recipe ')
    desired_size = num_check('how many serving are needed ')
    scale_factor = desired_size / serving_size

    if scale_factor < 0.25:
        sf_ok = input("Warning: this scale factor is very small "
                      "and you might struggle to accurately weigh"
                      "the ingredients. \n"
                      "do you want to keep going (type 'no' to change"
                      "your desired serving size )")
    elif scale_factor > 4:
        sf_ok = input("Warning: This scale factor is quite large - you might"
                      "have issues with mixing bowl space / oven space. \n"
                      "Do you want to keep goin (type 'no' to change"
                      "your desired serving size) ")



print('the scale factor is',scale_factor)
