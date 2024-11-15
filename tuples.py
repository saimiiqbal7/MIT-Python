
te = ()
ts = (2,)
t = (2,"Mit", 3)
tn = t + (4,5)


def qAndR(x,y):

    q = x//y
    r = x%y

    return (q,r)


def charCounts(s):

    vowels = "aeiou"
    const = "bcdfghjklmnpqrstvwxyz"

    countV = 0
    countC = 0

    for letter in s:
        if letter in vowels:
            countV += 1
        elif letter in const:
            countC += 1

    return (countV, countC)

print((charCounts("abcd")))