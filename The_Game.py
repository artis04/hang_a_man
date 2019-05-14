import length
maywords1 = []
maywords = []
ban = []
used = []
end = False

ans_word_len = length.length_of_word()

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
if ans_word_len == 9:
    w9 = '_'

print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9)

finding_letter = True

while finding_letter:
    for i in maywords:
        j = 0
        while j < ans_word_len:
            letter = i[j]
            if letter in ban or letter in used:
                j += 1
                #then letter is already told
            else:
                repeat = True
                choise = input('Does your word have any ' + letter + ' in it? Y or N:')
                while repeat:

                    choise = choise.lower()
                    if choise == 'y':
                        #repeat = False
                        where = input('in which place is letter ' + letter + '?')

                        #class right_letter:
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
                        else:
                            print('wrong location (you can type EXIT to exit this question')

                        maywords1 = []
                        for a in maywords:
                            if a[place - 1] == letter:
                                maywords1.append(a)
                        maywords = []
                        maywords = maywords1
                        maywords1 = []

                        print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9)

                        if len(maywords) == 1:
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
                        #maybe i could brake and use while

                    else:
                        repeat = True
                        print("sorry you didn't answer correctly")

                    if end:
                        break
                break
        break

    if end:
        break

if goal.lower() == 'y':
    print('Thanks for playing')
elif goal.lower() == 'n':
    print('WoW you beat me.')
    input('can you give me your word? :')
else:
    print('error')