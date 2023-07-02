pets=["dog","cat","parrot"]
for pet in pets:
    print(pet)
    if pet == "cat":
        break
#dog,cat


pets=["dog","cat","parrot"]
for pet in pets:
    if pet == "cat":
        break
    print(pet)
#dog


number=0
while number<10:
    print(number)
    if number == 5:
        break
    number += 1
#0,1,2,3,4,5


number=0
while number<10:
    if number == 5:
        break
    print(number)
    number += 1
#0,1,2,3,4


pets=["dog","cat","parrot"]
for pet in pets:
    if pet == "cat":
        continue
    print(pet)
#dog
#parrot


number=0
while number<10:
    if number == 5:
        continue
    print(number)
    number += 1
#0,1,2,3,4


pets=["dog","cat","parrot"]
for pet in pets:
    if pet == "cat":
        continue
    print(pet)
else:
    print("hello")
#dog,parrot,hello


pets=["dog","cat","parrot"]
for pet in pets:
    if pet == "cat":
        break
    print(pet)
else:
    print("hello")
#dog