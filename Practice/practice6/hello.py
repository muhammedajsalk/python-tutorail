my_list = [11, 5, 17, 18, 23, 50]
for item in my_list:
    if item%2==0:
        my_list.remove(item)
print(my_list)
#[11,5,17,23]