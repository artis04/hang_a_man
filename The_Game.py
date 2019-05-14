import length
maywords1 = []
maywords = []
ban = []

ans_word_len = length.length_of_word()

with open('words.txt', 'r') as f:
    maywords = [line.strip() for line in f]

for i in maywords:
    if len(i) == ans_word_len:
        g = i.lower()
        list.append(maywords1, g)
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

print(maywords)

finding_letter = True

while finding_letter:
    for i in maywords:
        j = 0
        while j < ans_word_len:
            letter = i[j]

            if letter in ban:
                pass
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
                        elif int(where) == 2 and w2 == '_':
                            w2 = letter
                        elif int(where) == 3 and w3 == '_':
                            w3 = letter
                        elif int(where) == 4 and w4 == '_':
                            w4 = letter
                        elif int(where) == 5 and w5 == '_':
                            w5 = letter
                        elif int(where) == 6 and w6 == '_':
                            w6 = letter
                        elif int(where) == 7 and w7 == '_':
                            w7 = letter
                        elif int(where) == 8 and w8 == '_':
                            w8 = letter
                        elif int(where) == 9 and w9 == '_':
                            w9 = letter
                        else:
                            print('wrong location (you can type EXIT to exit this question')


                        print(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5 + ' ' + w6 + ' ' + w7 + ' ' + w8 + ' ' + w9)
                        more = input('does this word have more ' + letter + '?')
                        more = more.lower()
                        if more == 'y':
                            pass
                        elif more == 'n':
                            repeat = False
                        else:
                            print('hey! you gave me incorrect answer!!')
                        #if word have that letter
                        ban.append(letter)

                    elif choise == 'n':
                        repeat = False
                        ban.append(letter)
                    else:
                        repeat = True
                        print("sorry you didn't answer correctly")

            j += 1

