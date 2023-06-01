x=input("enter a number: ")
if x.isdigit():
    if int(x) % 2 == 0:
        print(f"{x} is an even number.")
    else:
        print(f"{x} is an odd number.")
