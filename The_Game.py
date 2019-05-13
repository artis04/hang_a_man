import length
maywords1 = []
maywords = []

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
ban = []

print(maywords)

finding_letter = True

while finding_letter:
    for i in maywords:
        j = 0
        while j < ans_word_len:
            letter = i[j]

            if letter in ban:
                #then letter is already told
            else:
                #then letter is free to use


            j += 1

