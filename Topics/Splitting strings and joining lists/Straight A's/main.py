# put your python code here
grades = input()
grades = grades.split()
counter = 0

for gr in grades:
    if gr == 'A':
        counter += 1

print(round((counter / len(grades)), 2))