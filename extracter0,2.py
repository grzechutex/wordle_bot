slowa = []

with open('slowa.txt', encoding='utf-8') as words:
    for i in words:
        if len(i) == 12:
            slowa.append(i)
            print(i)

#print('marka' in slowa)

with open('slowa/slowa11txt','w',encoding='utf-8') as slowa5:
    for i in slowa:
        #slowa5.write('\n')
        slowa5.write(i)