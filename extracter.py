slowa = []
with open('slowa.txt', encoding='utf-8') as words:

    for i in words:
        lines = words.readline()
        if len(lines) == 5:
            with open('slowa5.txt','w', encoding='utf-8') as words5:
                words5.write('\n')
                words5.write(lines)
                #words5.close
                print(lines)
        #print(lines)

