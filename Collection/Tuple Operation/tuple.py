x=(1,2,3)
y=(4,5,6)
print(x+y)
#(1,2,3,4,5,6)

print(x*2)
#(1,2,3,1,2,3)

print(x.index(2))
#1

print(1 not in x)
#false

names=("a","b")
student={}
student[names]="Hello"
print(student)
#{('a','b'):'Hello'}

bio=("Ajsal",10,"c")
name, std_class, div = bio
print(name)
#Ajsal
*others,div=bio
print(div)
#0
print(others)
#['Ajsal', 10]

a=10
b=20
b,a=a,b
print(b)
#10