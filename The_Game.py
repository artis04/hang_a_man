import collections
repeat_goal = True

while repeat_goal:
    may_words1 = []
    may_words = []
    ban = []
    used = []
    end = False
    ans_word_len = 0
    mistakes = 0
    nex = ''
    place = ''
    goal = ''
    repeat = True
    file = ''
    lost = False
# not gut... if there is only one a letter, it will save words with more a letters
    while repeat:
        carpet = input('do you want to play with all or most used words? :')
        if carpet.lower() == 'all' or carpet.lower() == 'all words':
            file = 'words.txt'
            repeat = False
        elif carpet.lower() == 'most' or carpet.lower() == 'most used' or carpet.lower() == 'most words':
            file = 'most.txt'
            repeat = False
        else:
            print(
                '''
                wrong answer
                you can answer by
                all / all words
                most / most used / most words           
            '''
            )
            repeat = True

    correct = True
    while correct:
        length = input('how long is your word? form 3 to 14:')

        if int(length) < 3 or int(length) > 31:
            print('sorry you entered wrong number ' + length + 'is not between 3 and 14')
        else:
            ans_word_len = int(length)
            correct = False

    with open(file, 'r') as f:
        may_words = [line.strip() for line in f]

    for i in may_words:
        if len(i) == ans_word_len:
            g = i.lower()
            may_words1.append(g)
    may_words = may_words1
    may_words1 = ''

    # now i have only length of word
    w1 = '_'
    w2 = '_'
    w3 = '_'
    w4 = ''
    w5 = ''
    w6 = ''
    w7 = ''
    w8 = ''
    w9 = ''
    w10 = ''
    w11 = ''
    w12 = ''
    w13 = ''
    w14 = ''

    # class gettingW:
    if ans_word_len >= 4:
        w4 = '_'
    if ans_word_len >= 5:
        w5 = '_'
    if ans_word_len >= 6:
        w6 = '_'
    if ans_word_len >= 7:
        w7 = '_'
    if ans_word_len >= 8:
        w8 = '_'
    if ans_word_len >= 9:
        w9 = '_'
    if ans_word_len >= 10:
        w10 = '_'
    if ans_word_len >= 11:
        w11 = '_'
    if ans_word_len >= 12:
        w12 = '_'
    if ans_word_len >= 13:
        w13 = '_'
    if ans_word_len == 14:
        w14 = '_'

    print(w1+' '+w2+' '+w3+' '+w4+' '+w5+' '+w6+' '+w7+' '+w8+' '+w9+' '+w10+' '+w11+' '+w12+' '+w13+' '+w14)

    finding_letter = True
    while finding_letter:
        fax = []
        words = []
        necessary = 0
        for i in may_words:
            j = 0
            while j < len(i):
                a = i[j]
                fax.append(a)
                j += 1
        counter = collections.Counter(fax)
        words = counter.most_common()
        if ban != [] or used != []:
            ged_repeat = True
        else:
            ged_repeat = False
            nex = words[0]
        while ged_repeat:
            nex = words[necessary]
            for q in ban:

                if nex[0] == q:
                    necessary += 1
                    ged_repeat = True
                else:
                    ged_repeat = False

            for q in used:
                if nex[0] == q:
                    necessary += 1
                    ged_repeat = True
                    break
                else:
                    ged_repeat = False
        letter = nex[0]
        j = 0

        if letter in ban or letter in used:
            pass
            # then letter is already told
        else:
            repeat = True
            # print(may_words)
            choice = input('Does your word have any ' + letter + ' in it? Y or N:')
            while repeat:
                choice = choice.lower()
                if choice == 'y':
                    where = input('in which place is letter ' + letter + '? (you can use exit)')

                    if where.lower() == 'exit':
                        repeat = False
                    elif int(where) == 1 and w1 == '_':
                        w1 = letter
                        place = 1
                    elif int(where) == 2 and w2 == '_':
                        w2 = letter
                        place = 2
                    elif int(where) == 3 and w3 == '_':
                        w3 = letter
                        place = 3
                    elif int(where) == 4 and w4 == '_':
                        w4 = letter
                        place = 4
                    elif int(where) == 5 and w5 == '_':
                        w5 = letter
                        place = 5
                    elif int(where) == 6 and w6 == '_':
                        w6 = letter
                        place = 6
                    elif int(where) == 7 and w7 == '_':
                        w7 = letter
                        place = 7
                    elif int(where) == 8 and w8 == '_':
                        w8 = letter
                        place = 8
                    elif int(where) == 9 and w9 == '_':
                        w9 = letter
                        place = 9
                    elif int(where) == 10 and w10 == '_':
                        w10 = letter
                        place = 10
                    elif int(where) == 11 and w11 == '_':
                        w11 = letter
                        place = 11
                    elif int(where) == 12 and w12 == '_':
                        w12 = letter
                        place = w12
                    elif int(where) == 13 and w13 == '_':
                        w13 = letter
                        place = w13
                    elif int(where) == 14 and w14 == '_':
                        w14 = letter
                        place = w14
                    else:
                        print('wrong location (you can type EXIT to exit this question')

                    may_words1 = []
                    for a in may_words:
                        if a[place - 1] == letter:
                            may_words1.append(a)
                    may_words = may_words1
                    may_words1 = []

                    print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9
                          + ' ' + w10 + ' ' + w11 + ' ' + w12 + ' ' + w13 + ' ' + w14)

                    if len(may_words) == 1:
                        print('##############################')
                        print('##############################')
                        goal = input('Is your word ' + may_words[0] + ' ?')
                        end = True

                    if end:
                        break

                    more = input('does this word have more ' + letter + '?')
                    more = more.lower()
                    if more == 'y':
                        pass
                    elif more == 'n':
                        repeat = False
                        # here i should make system that removes word which have that letters but in wrong place [[[HARD
                    else:
                            print('hey! you gave me incorrect answer!!')
                    used.append(letter)

                elif choice == 'n':

                    mistakes += 1
                    if mistakes == 1:
                        print('''
                        
                        




                        _____________
                        ''')

                    elif mistakes == 2:
                        print('''
                        
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |_____________
                        ''')

                    elif mistakes == 3:
                        print('''
                         _______
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |_____________
                        ''')

                    elif mistakes == 4:
                        print('''
                         _______
                        |     |
                        |     
                        |   
                        |
                        |
                        |
                        |
                        |
                        |_____________
                        ''')

                    elif mistakes == 5:
                        print('''
                         _______
                        |     |
                        |    /¯\ 
                        |    \_/
                        |
                        |
                        |
                        |
                        |
                        |_____________
                        ''')

                    elif mistakes == 6:
                        print('''
                         _______
                        |     |
                        |    /¯\ 
                        |    \_/
                        |     |
                        |     |
                        |
                        |
                        |
                        |_____________
                        ''')
                    elif mistakes == 7:
                        print('''
                         _______
                        |     |
                        |    /¯\ 
                        |    \_/
                        |     |
                        |     |
                        |    / 
                        |   /  
                        |
                        |_____________
                        ''')
                    elif mistakes == 8:
                        print('''
                         _______
                        |     |
                        |    /¯\ 
                        |    \_/
                        |     |
                        |     |
                        |    / \ 
                        |   /   \  
                        |
                        |_____________
                        ''')
                    elif mistakes == 9:
                        print('''
                         _______
                        |     |
                        |    /¯\ 
                        |    \_/
                        |    /|
                        |   / |
                        |    / \ 
                        |   /   \  
                        |
                        |_____________
                        ''')
                    elif mistakes == 10:
                        print('''
                         _______
                        |     |
                        |    /¯\ 
                        |    \_/
                        |    /|\ 
                        |   / | \ 
                        |    / \ 
                        |   /   \  
                        |
                        |_____________
                        
    GAME OVER THANKS FOR PLAYING AI WAS NOT SMART ENOUGH
                        ''')
                        lost = True
                        end = True

                    repeat = False
                    ban.append(letter)
                    may_words_ban = []
                    for s in may_words:
                        b = 0
                        while b < ans_word_len:
                            if s[b] in ban:
                                may_words_ban.append(s)
                                break
                            b += 1
                    for s in may_words_ban:
                        if may_words[0] == 'dog':
                            pass
                        may_words.remove(s)
                    may_words_ban = []
                    print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9
                          + ' ' + w10 + ' ' + w11 + ' ' + w12 + ' ' + w13 + ' ' + w14)

                    if len(may_words) == 1:
                        print('##############################')
                        print('##############################')
                        goal = input('Is your word ' + may_words[0] + ' ?')
                        end = True

                else:
                    repeat = True
                    print("ERROR PLEASE REOPEN APPLICATION sorry you didn't answer correctly")
                if end:
                    break
            if end:
                break
        if end:
            break

    if goal.lower() == 'y':
        repeat_goal = False
        print('Thanks for playing')
        again = input('Do you want to play again?')
        if again.lower() == 'y':
            repeat_goal = True
    elif goal.lower() == 'n':
        print('WoW you beat me.')
        print('what was your word?')
        new_word = input(':')
        with open('words.txt', 'a') as words:
            words.write('\n')
            words.write(new_word)
    elif lost:
        print("that was a great play, but AI couldn't guess that word")
    else:
        print('game has ended with error')
