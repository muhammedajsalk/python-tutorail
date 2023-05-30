string ="pinapple"
"apple" in string
#true
"orange" in string
#false

email = "ajsalmuhammed747@gmail.com"
email.startswith("ajsal")
#true
email.startswith("com")
#false
email.endswith("ajsal")
#false
email.endswith("com")
#true

string.startswith("a")
#false
string.startswith("a",3)
#true
string.endswith("e",3,6)
#false
string.endswith("e",3)
#true

string.find("apple")
#3
string.find("ple")
#5
string.find("orange")
#-1

string.count("p")
#3
string.count("i")
#1
string.count("k")
#0
