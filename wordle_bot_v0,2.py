words = []
possible_words = []
lettersD = []
lettersDM = []
lettersZ = []
a = input('Ile liter ma twoje wordle?: ')

letter_dict = {
    'q': 0,
    'w': 0,
    'e' : 0,
    'r' : 0,
    't' : 0,
    'y' : 0,
    'u' : 0,
    'i' : 0,
    'o' : 0,
    'p' : 0,
    'a' : 0,
    's' : 0,
    'd' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'z' : 0,
    'x' : 0,
    'c' : 0,
    'v' : 0,
    'b' : 0,
    'n' : 0,
    'm' : 0,
    'ę' : 0,
    'ó' : 0,
    'ą' : 0,
    'ś' : 0,
    'ł' : 0,
    'ż' : 0,
    'ź' : 0,
    'ć' : 0,
    'ń' : 0,
}


with open('slowa/slowa'+a+'.txt', encoding='utf-8') as f:
    for i in f:
        word = f.readline()
        #print(word)
        words.append(word)

print(words)

def letter_counter(litera):
    letter_dict[litera] += 1
    return letter_dict




while True:
    a = 0
    #numbers = [1,2,3,4,5]
    toDo = input('Dobra litera - D, Dobra litera w dobrym miejscu - DM, zła litera - Z, ENTER - koniec: ')
    toDo.upper()

#if the letter is right but in wrong place
    if toDo == 'D':
        letter = input('Wprowadz litere: ')
        letter.lower()
        #if letter in lettersD:
        #    break
        lettersZ.append(letter)
        a = 1
        place = int(input('Wprowadz miejsce: '))-1
        letter.lower()
        for i in words:
            #print(i)
            if letter in i and letter != i[place]:
                possible_words.append(i)

#if the letter is in right place
    elif toDo == 'DM':
        letter = input('Wprowadz litere: ')
        letter.lower()
        #if letter in lettersDM:
        #    break
        lettersZ.append(letter)
        a = 1

        place = int(input('Wprowadz miejsce: '))-1
        #numbers.remove(place)
        for i in words:
            #print(i)
            if letter == i[place]:
                possible_words.append(i)
            #elif letter == i[numbers[0]] or letter == i[numbers[1]] or letter == i[numbers[2]] or letter == i[numbers[3]]:
                #possible_words.append(i)

#if the letter is wrong
    elif toDo == 'Z':
        letter = input('Wprowadz litere: ')
        letter.lower()
        if letter in lettersZ:
            print('Litera użyta')
            #break
        else:
            lettersZ.append(letter)
            a = 1
            for i in words:
                #print(i)
                if letter in i:
                    a = 1
                else:
                    possible_words.append(i)
    
    elif toDo == '':
        exit()

    #else:
    #   with open(input(''))
    if a == 1:
        words = possible_words
        possible_words = []
        print(words)