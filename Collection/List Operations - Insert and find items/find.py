x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
x.insert(2,100)
print(x)
#[1, 2, 100, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1]

x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
x.insert(len(x),100)
print(x)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2,1,100]

x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
print(5 in x)
#true

x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
print(15 in x)
#false

x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
print(5 not in x)
#false

x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
print(20 not in x)
#true

x=[1,2,3,4,5,6,7,8,9,10,1,2,1]
print(x.count(1))
#3




