def add(x,y,**kwargs):
    print(kwargs)
    return x+y
a= add(10,20,hello=30,hi=20,z=40)

print(a)

#{'hello': 30, 'hi': 20, 'z': 40}
#30

def add(x,y,**kwargs):
    print(kwargs["hi"])
    return x+y
a= add(10,20,hello=30,hi=20,z=40)

print(a)

#20
#30