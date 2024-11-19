
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