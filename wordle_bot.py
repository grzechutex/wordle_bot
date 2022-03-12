words = []
possible_words = []

with open('slowa5.txt', encoding='utf-8') as f:
    for i in f:
        word = f.readline()
        print(word)
        words.append(word)

print(words)

while True:
    toDo = input('Dobra litera - D, Dobra litera w dobrym miejscu - DM, zła litera - Z, ENTER - koniec: ')

    if toDo == 'D':
        letter = input('Wprowadz litere: ')
        for i in words:
            print(i)
            if letter in i:
                possible_words.append(i)
    
    elif toDo == 'DM':
        letter = input('Wprowadz litere: ')
        place = int(input('Wprowadz miejsce: '))-1
        for i in words:
            print(i)
            if letter == i[place]:
                possible_words.append(i)

    elif toDo == 'Z':
        letter = input('Wprowadz litere: ')
        for i in words:
            print(i)
            if letter in i:
                print('')
            else:
                possible_words.append(i)
    words = possible_words
    possible_words = []
    print(words)