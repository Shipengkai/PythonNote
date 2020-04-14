# try:
#     age = int(input('Age: '))
# except (ValueError, ZeroDivisionError) as ex:  # ,comma
#     print('You didn\'t enter a valid age')
#     print(ex, type(ex))
# else:
#     print('No exceptions were thrown.')
# finally:
#     pass


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('age cannot be 0 or less')
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as e:
    print(e)
