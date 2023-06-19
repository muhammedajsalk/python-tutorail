def add(x,y,z=100):
    print(y)
    return x+y+z

a=add(y=100,x=20)
print(a)
#100
#200



def add(x,y,z=100):
    print(y)
    return x+y+z

a=add(y=100,x=20,z=10)
print(a)
#100
#130


def add(x,y,z=100):
    print(y)
    return x+y+z

a=add(10,100,10)
print(a)
#100
#130
