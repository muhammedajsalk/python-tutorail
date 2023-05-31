sentance="my name is Ajsal. i'am studing in 10 B"
name="Ajsal"
class_="10"
division="c"
print("my name is "+name+".I'am studing in "+class_+" "+division)
#my name is Ajsal.I'am studing in 10 c


new="My name is %s. I'm Studing in %s %s" %(name,class_,division)
#My name is Ajsal. I'm studing in 10 c


11/3
#3.666666666665
print('%.3f' %(11/3))
#3.667
print('%.2f' %(11/3))
#3.67


new = "My name is {}. i'm Studing in {} {}.".format("Ajsal","10","c")
print(new)
#My name is Ajsal. i'm Studing in 10 c.


new = "My name is {1}. i'm Studing in {0} {2}.".format("Ajsal","10","c")
#My name is 10. i'm Studing in Ajsal c.


new = "My name is {name}. i'm Studing in {class_} {division}.".format(name="Ajsal",class_="10",division="c")
#My name is Ajsal. i'm Studing in 10 c.


name="Ajsal"
class_="10"
division="c"
sent="My name is f'{name}. iam Studying in f'{class_} f'{divition}
print(sent)
#My name is Ajsal. iam Studing in 10 c


name="Ajsal"
class_="10"
division="c"
new=f"My name is {name}. I'm studing in {class_} {division}"
#My name is Ajsal.I'm studing in 10 c




