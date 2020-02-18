def not_blank(question):
    valid = False
    while valid == False:
        response = input(question)
        if response == "":
            continue
        else:
            return(response)








recipe_name = not_blank('what would you like to make')
print(' you are making ',recipe_name)