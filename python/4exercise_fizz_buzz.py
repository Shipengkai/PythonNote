# this is an exercise
def fizz_buzz(input):
    fizz = not bool(input % 3)
    buzz = not bool(input % 5)
    if fizz and buzz:
        return 'Fizz_Buzz'
    elif buzz:
        return 'Buzz'
    elif fizz:
        return 'Fizz'
    return input


message = ''
while message.lower() != 'quit':
    message = input('> ')
    print(fizz_buzz(int(message)))
