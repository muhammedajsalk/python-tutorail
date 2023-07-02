word = "hello54236726hdfjds"
sum=0
for x in word:
    if x.isdigit():
        sum += int(x)
print(sum)
#35


#another option
word = "hello54236726hdfjds"
def calculate(string):
    sum=0
    for x in string:
        if x.isdigit():
            sum += int(x)
    return sum
print(calculate(word))
#35

