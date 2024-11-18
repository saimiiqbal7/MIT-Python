
def bisectionCube(x):

    #x is the number we want to find the the cube root of
    
    epsilon = 0.01
    #acceptable error margin

    low = 0
    #Start with the lower bound of 0

    high = x
    #cube root can not be larger than the number

    guess = (high+low)/2.0
    #Initial guess is halfway point

    while abs(guess**3 - x) >= epsilon:

        if guess**3 < x:
            low = guess
        else:
            high = guess

        guess = (high+low)/2.0

    return guess

print(bisectionCube(27))





