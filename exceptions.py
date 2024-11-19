

def sumDigits(s):

    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
            print(f"Adding {val}")
        except:
            print(f"Not an Int {char}")

    return total

def divide():

    try:

        a = int(input("Enter a number "))
        b = int(input("Enter another number "))
        return a/b
    
    except:
        return "Inputs not valid"
        

def pairwise(lnum, lden):

    '''Both inputs are non empty lists of equal lengths'''

    l = []

    for i in range(len(lnum)):

        try:
            l.append(lnum[i]/lden[i])
        
        except:
            print("code has error")

    
    return l






