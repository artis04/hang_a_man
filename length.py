def length_of_word():
    correct = False
    while correct != True:
        length = input('how long is your word? form 3 to 14:')

        if int(length) < 3 or int(length) > 14:
            print('sorry you entered worng number ' + length + 'is not between 3 and 14')
        else:
            correct = True


    return int(length)