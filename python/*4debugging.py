# debugging
def multiply(*numbers):
    multiply = 1
    for number in numbers:    # numbers is a tuple      AAAAAAAAAAAAAAA
        multiply *= number
    return multiply


print('start')
x = multiply(1, 2, 3, 4, 5)
print(x)
