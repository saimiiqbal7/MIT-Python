

'''
Convert Decimal to Binary in Python
'''
num = 10 #ENTER A POSITIVE NUMBER HERE

result = ''
if num == 0:
    result = '0'

while num > 0:

    result = str(num%2) + result
    num = num//2


print(result)


 



