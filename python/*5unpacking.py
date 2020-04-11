numbers = [1, 2, 3]
print(*numbers)
values = [*range(5), *'Hello']
print(values)
first = {'x': 1, 'y': 2}
second = {'x': 10}
print(*first)
combined = {**first, **second, 'z': 20}
print(combined)
