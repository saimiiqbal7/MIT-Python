
def doTwice(n, fn):
    return fn(fn(n))

print(doTwice(4, lambda x: x**2))
 