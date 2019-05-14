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
                while repeat:
                    choise = input('Does your word have any ' + letter + ' in it? Y or N:')
                    choise = choise.lower()
                    if choise == 'y':
                        repeat = False
                        where = input('in which place is letter ' + letter + '?')
                        #if word have that letter

                    elif choise == 'n':
                        repeat = False
                        ban.append(letter)
                    else:
                        repeat = True
                        print("sorry you didn't answer correctly")

            j += 1

