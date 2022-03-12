slowa = []
a = 0
slowabezn = []

with open('slowa.txt', encoding='utf-8') as words:

    for i in words:
        lines = words.readline()
        if len(lines) == 6:
            slowa.append(lines)
            print(lines)
    for i in slowa:
        print(i)
        slowo = slowa[a]
        slowabezn.append(slowo)
        a = a + 1
print(slowabezn[1])

with open('slowa5.txt','w',encoding='utf-8') as slowa5:
    for i in slowabezn:
        #slowa5.write('\n')
        slowa5.write(i)