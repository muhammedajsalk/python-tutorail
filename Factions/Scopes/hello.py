a=10#Global scope

def add(x,y):
    print(a)
    return x+y

z=add(10,20)
print(z)

#10
#30

a=10#Global scope

def add(x,y):
    print(a)
    b=20#Local scope
    print(b)
    return x+y

z=add(10,20)
print(z)
print(b)# b is not deffined

#10
#20
#30