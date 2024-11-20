
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

l = [1,2,3,4,5,6]
m = l.copy()
k = l
k[0] = 2
l[1] = 3
print(l)
print(m)