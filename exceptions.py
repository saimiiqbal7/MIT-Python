

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
        

print(divide())