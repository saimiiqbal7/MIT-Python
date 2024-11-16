
def makeOrdList(n):

    l = []
    for i in range(n+1):
        l.append(i)

    return l

def removeEl(l,e):

    newL = []
    for i in l:
        if i is not e:
            newL.append(i)
    
    return newL

def countWords(sen):

    l = sen.split(' ')
    return len(l)


