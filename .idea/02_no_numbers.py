
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response == '':
            continue
        else:
            print('thank you')
            break




recipe_name = not_blank('? ')
