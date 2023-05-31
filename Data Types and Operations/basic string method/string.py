#.........................................................................
#.........................................................................
#Basic String Methods
#.........................................................................
#.........................................................................


message="hello guys what can i do for you"
print(message.upper())
#console= HELLO GUYS WHAT CAN I DO FOR YOU
#message is not changed
print(message)
#hello guys what can i do for you

title_message = message.title()
print(title_message)
#console=Hello Guys What Can I Do For You

message.lower()
#'hello guys what can i do for you'

message.capitalize()
#'Hello guys what can i do for you'

message.replace("guys", "Boys")
#'hello Boys what can i do for you'

whitespace_string = "     hey     "
whitespace_string.lstrip()
#'hey     '
whitespace_string.rstrip()
#'     hey'
whitespace_string.strip()
#'hey'

#example strip
normal_string ="incompokertialtations"
normal_string.lstrip("is")
#'ncompokertialtations'
normal_string.rstrip("is")
#'incompokertialtation'
normal_string.strip("is")
#'ncompokertialtation'

word="Mississippi"
print(word.rstrip("ips"))
#M
print(word.lstrip("ips"))
#Mississippi
>>> print(word.lstrip("M"))   
#ississippi
