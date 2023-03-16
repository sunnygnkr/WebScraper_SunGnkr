list1 = [1, 2, 3, 4]

list2 = list(map(lambda num: num ** 2, list1))
print(list2)


def is_Even(num):
    return num % 2 == 0


# The above function can be replaced by lambda function
list3 = list(filter(lambda x: x % 2 == 0, list1))
print(list3)
