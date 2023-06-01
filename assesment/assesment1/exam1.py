string_example = "Hello, World!"


slice1 = string_example[7:]
print(slice1)  # Output: "World!"


slice2 = string_example[:5]
print(slice2)  # Output: "Hello"


slice3 = string_example[7:12]
print(slice3)  # Output: "World"


slice4 = string_example[-6:-1]
print(slice4)  # Output: "World"


slice5 = string_example[::2]
print(slice5)  # Output: "Hlo ol!"


slice6 = string_example[::-1]
print(slice6)  # Output: "!dlroW ,olleH"
