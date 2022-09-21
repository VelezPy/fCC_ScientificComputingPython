fname = input('Enter file: ')
if len(fname) < 1 : fname = 'mboxshort.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

print(di)

#now we want to find the most common word
largest = -1 
for k, v in di.items() :
    print (k,v)
    if v > largest:
        largest = v
        theword = k

print ('Done', theword, largest)
    