words = []

with open('slowa5.txt', encoding='utf-8') as f:
    for i in f:
        word = f.readline()
        print(word)
        words.append(word)

#print(words)

while True:
    toDo = input('Dobra litera - D, Dobra litera w dobrym miejscu - DM, zła litera - Z: ')

    if toDo == 'D':
        letter = input('Wprowadz litere: ')
        
        for i in words:
            if letter in i:
                break
            else:
                words[a]