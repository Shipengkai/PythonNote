numbers = [1, 2, 2, 3, 4]
first = set(numbers)
second = {2, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
print((first | second) - (first & second))
# unorder collection, can not access use index
