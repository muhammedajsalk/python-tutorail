mystr="Hello World"

mystr.split()
#['Hello', 'World']
mystr.split("e")
#['H', 'llo World']
mystr.split("l")
#['He', '', 'o Wor', 'd']
mystr.split("d")
#['Hello Worl', '']
mystr.split("Wo")
#['Hello ', 'rld']

mylist= ['Hello', 'World']
newstr="".join(mylist)
newstr
#'HelloWorld'
newstr=" ".join(mylist)
newstr
#'Hello World'
newstr="_".join(mylist)
newstr
#'Hello_World'