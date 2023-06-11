student={
    "name":"Ajsal",
    "class":1,
    "division":"c",
    "subjects":["Malayalam","English"]
}
x=student.pop("subjects")
print(student)
print(x)
#{'name': 'Ajsal', 'class': 1, 'division': 'c'}
#['Malayalam', 'English']

del student["division"]
print(student)
#{'name': 'Ajsal', 'class': 1}

student.clear()
print(student)
#{}