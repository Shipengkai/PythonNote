# debugging
def multiply(*numbers):
    multiply = 1
    for number in numbers:
        multiply *= number
        return multiply


print('start')
x = multiply(1, 2, 3, 4, 5)
print(x)
