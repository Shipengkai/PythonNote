
# Section A     function (parameters & arguments)

"""
The difference between parameters and arguments.
Name is a parameter and spk is an argument.
So an argument is the actual value for a given parameter.
"""


def greet(name):
    print(f'Hello {name}!')


print(greet('spk'))

# Section B     two types of function

# 1- Perform a task. Return None.
# 2- Return a value


def get_greeting(name):
    return f"Hi {name}!"


message = get_greeting('spk')
file = open("4content.txt", "w")
file.write(message)


# Section C     tricks

# Default arguments
def increment(number, by=1):
    return number + by


print(increment(2, 2), increment(2))


# xargs
def multiply(*numbers):
    multiply = 1
    for number in numbers:
        multiply *= number
    return multiply


x = multiply(1, 2, 3, 4, 5)
print(x)


# xxargs        user is a dictionary
def save_user(**user):
    print(f"{user}\n{user['id']}\n{user['name']}\n{user['age']}")


save_user(id=1, name='John', age=22)
