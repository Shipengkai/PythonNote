# comparison
print(ord('a'))
# ...
print('b' > 'a' and 'b' > 'B')
# ...


# if
# __init__
temperature = 35
if temperature > 30:
    print("It's warm.")
    print('Drink water.')
elif temperature > 20:
    print("It's nice.")
else:
    print("It is cold.")
print('Done')
# Ternary Operator
age = 22
"""
if age >= 18:
    message = 'Eligible'
else:
    message = 'Not eligible'
"""
message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)


# for
successful = True
i = 0
for number in range(1, 10, 2):
    i += 1
    print('Attempt', number, '.' * i)
    if successful:
        print('Successful')
        break
else:
    print(f'Attempted {i} times and failed')

# Iterable
print(type(range(5)))
for x in "python":
    print(x)
for x in ((1, 2), (2, 3)):
    print(x)


# while
number1 = 100
while number1 > 0:
    print(number1)
    number1 //= 2


# 3.13 infinit loops
command = ''
while command.lower() != 'quit':
    command = input('> ')
    print("ECHO", command)
