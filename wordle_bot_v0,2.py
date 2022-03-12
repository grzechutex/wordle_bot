words = []
possible_words = []
a = input('Ile liter ma twoje wordle?: ')


with open('slowa/slowa'+a+'.txt', encoding='utf-8') as f:
    for i in f:
        word = f.readline()
        #print(word)
        words.append(word)

print(words)

while True:
    #numbers = [1,2,3,4,5]
    toDo = input('Dobra litera - D, Dobra litera w dobrym miejscu - DM, zła litera - Z, ENTER - koniec: ')
    toDo.upper()

    if toDo == 'D':
        letter = input('Wprowadz litere: ')
        place = int(input('Wprowadz miejsce: '))-1
        letter.lower()
        for i in words:
            #print(i)
            if letter in i and letter != i[place]:
                possible_words.append(i)
    
    elif toDo == 'DM':
        letter = input('Wprowadz litere: ')
        letter.lower()
        place = int(input('Wprowadz miejsce: '))-1
        #numbers.remove(place)
        for i in words:
            #print(i)
            if letter == i[place]:
                possible_words.append(i)
            #elif letter == i[numbers[0]] or letter == i[numbers[1]] or letter == i[numbers[2]] or letter == i[numbers[3]]:
                #possible_words.append(i)

    elif toDo == 'Z':
        letter = input('Wprowadz litere: ')
        letter.lower()
        for i in words:
            #print(i)
            if letter in i:
                print('')
            else:
                possible_words.append(i)
    words = possible_words
    possible_words = []
    print(words)