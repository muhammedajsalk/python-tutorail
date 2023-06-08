student={
    "name":"Ajsal",
    "class":1,
    "division":"c",
    "subject":["malayalam","english"]
} 
print(student)
#{'name': 'Ajsal', 'class': 1, 'division': 'c'}

print(student["name"])
#Ajsal

student["marks"]=[10,20]
print(student)
#{'name': 'Ajsal', 'class': 1, 'division': 'c', 'subject': ['malayalam', 'english'], 'marks': [10, 20]}