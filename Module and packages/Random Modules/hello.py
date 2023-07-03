import random

x=random.random()
print(x)
#0-1


y=random.uniform(1,100)
print(y)
#1-100


z=random.randint(1,100)
print(z)
#1-100


list_iteams=[1,2,3,4,5]
a=random.choice(list_iteams)
print(a)
#listnte ullil ninn random choices therum


b=random.randrange(0,100,5)
print(b)
#0-100 5 nte multple


c=[1,2,3,4,5,6,7,8,9]
random.shuffle(c)
print(c)
#random shufling


d=[1,2,3,4,5,6,7,8,9]
x=random.sample(d,2)
print(x)
#random ayyitt list ninn 2nam items idkum



