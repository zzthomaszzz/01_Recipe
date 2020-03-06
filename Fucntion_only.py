def not_blank(question):
    valid = False
    while valid == False:
        response = input(question)
        blank = 'this can not be blank'
        if response == '':
            print(blank)
            continue
        else:
            break
recipe_name = not_blank('what is the recipe name ')
print('thank you')