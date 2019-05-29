import collections
repeat_goal = True

while repeat_goal:
    maywords1 = []
    maywords = []
    ban = []
    used = []
    end = False
#not gut... if there is only one a letter, it will save words with more a letters

    correct = True
    while correct:
        length = input('how long is your word? form 3 to 14:')

        if int(length) < 3 or int(length) > 14:
            print('sorry you entered worng number ' + length + 'is not between 3 and 14')
        else:
            ans_word_len = int(length)
            correct = False


    with open('words.txt', 'r') as f:
        maywords = [line.strip() for line in f]

    for i in maywords:
        if len(i) == ans_word_len:
            g = i.lower()
            maywords1.append(g)
    maywords = maywords1
    maywords1 = ''

    #now i have only length of word
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

    #class gettingW:
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

    print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9 + ' ' + w10 + ' ' + w11 + ' ' + w12 + ' ' + w13 + ' ' + w14)

    finding_letter = True
    fax = []
    while finding_letter:
        for i in maywords:
            r = 0
            j = 0
            while j < len(i):
                while r < len(i):
                    a = i[r]
                    fax.append(a)
                    r += 1
                counter = collections.Counter(fax)
                words = counter.most_common()
                nex = words[0]
                letter = nex[0]
                j = 0
                if letter in ban or letter in used:
                    j += 1
                    #then letter is already told
                else:
                    repeat = True
                    print(maywords)
                    choise = input('Does your word have any ' + letter + ' in it? Y or N:')
                    while repeat:

                        choise = choise.lower()
                        if choise == 'y':
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

                            maywords1 = []
                            for a in maywords:
                                if a[place - 1] == letter:
                                    maywords1.append(a)
                            maywords = []
                            maywords = maywords1
                            maywords1 = []

                            print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9 + ' ' + w10 + ' ' + w11 + ' ' + w12 + ' ' + w13 + ' ' + w14)


                            if len(maywords) == 1:
                                print('##############################')
                                print('##############################')
                                goal = input('Is your word '+ maywords[0] + ' ?')
                                end = True

                            if end:
                                break

                            more = input('does this word have more ' + letter + '?')
                            more = more.lower()
                            if more == 'y':
                                pass
                            elif more == 'n':
                                repeat = False
                            else:
                                print('hey! you gave me incorrect answer!!')
                            #if word have that letter
                            used.append(letter)

                        elif choise == 'n':
                            repeat = False
                            ban.append(letter)
                            maywords_ban = []
                            for s in maywords:
                                b = 0
                                while b < ans_word_len:
                                    if s[b] in ban:
                                        maywords_ban.append(s)
                                        break
                                    b += 1
                            for s in maywords_ban:
                                if maywords[0] == 'dog':
                                    pass
                                maywords.remove(s)
                            maywords_ban = []
                            print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9 + ' ' + w10 + ' ' + w11 + ' ' + w12 + ' ' + w13 + ' ' + w14)
                        else:
                            repeat = True
                            print("sorry you didn't answer correctly")
                        if end:
                            break
                    if end:
                        break
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
        #input('can you give me your word? :')
    else:
        print('game has ended')