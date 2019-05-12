import length
maywords1 = []
maywords = []

ans_word_len = length.length_of_word()

with open('words.txt', 'r') as f:
    maywords = [line.strip() for line in f]

for i in maywords:
    if len(i) == ans_word_len:
        list.append(maywords1, i)
maywords = maywords1
maywords1 = ''

