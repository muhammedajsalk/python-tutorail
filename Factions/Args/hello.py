def add(x,y,*args):
    print(args)
    return x+y
a= add(10,20,30,40,50)

print(a)
#(30,40,50)
#30

def add(x,y,*args):
    print(args[1])
    return x+y
a= add(10,20,30,40,50)

print(a)
#40
#30