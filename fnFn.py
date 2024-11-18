
y = 2

def makeProd(a):

    def g(b):
        return a*b+y
    
    return g

val = makeProd(2)(3)
print(val)