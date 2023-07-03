integer=input("Enter an Integer: ")
try:
    print(int(integer))
except:
    print("Error")


integer=input("Enter an Integer: ")
try:
    print(int(integer))
except ValueError:
    print("Error")


integer=input("Enter an Integer: ")
try:
    print(int(integer))
except ValueError:
    print("Error")
else:
    print("Else Block")


integer=input("Enter an Integer: ")
try:
    print(int(integer))
except ValueError:
    print("Error")
else:
    print("Else Block")
finally:
    print("Finally Block")