
#myDict = {} Empty

grades = {'Ana': 'B', 'Matt': 'A', 'Saim': 'A', 'Linta': 'A+'}

grades['Alina'] = 'A'
grades['Linta'] = 'B'

print('Saim' not in grades)

def findGrades(grades, students):

    l = []
    for student in students:
        l.append(grades[student])
    
    return l

print(findGrades(grades, ['Saim','Linta', 'Alina']))

def find(ld, k):

    for l in ld:
        if k in l:
            return True
    
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1,3:9,4:16,5:25}

print(find([d1,d2,d3], 2))
print(find([d1,d2,d3], 25))

l = list(grades.items())
print(l)

for item in grades.items():
    print(item)

for key in grades.keys():
    print(type(key))
    print(key)

for value in grades.values():
    print(value)

g = {'Saim': {'mq':[5,4,4], 'ps': [10,9,9], 'fin': 'A'},
     'Linta': {'mq':[6,8,4], 'ps': [10,10,10], 'fin': 'A'}} 

print(g['Linta']['ps'])