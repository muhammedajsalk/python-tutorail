student={
    "name":"Ajsal K",
    "class":10,
    "division":"D"
}

for item in student:
    print(item)
#name,class,division


for item in student.values():
    print(item)
#Ajsal K,10,D


for item in student.keys():
    print(item)
#name,class,division


for item in student.keys():
    print(student[item])
#Ajsal K,10,D


for key,value in student.items():
    print(key)
    print(value)
#name Ajsal K class 10 divition D
