# Section A     list
def kind_of_lists():
    letters = ['a', 'b', 'c']
    matrix = [[0, 1], [2, 3]]
    zeros = [0] * 5
    combined = zeros + letters
    numbers = list(range(20))
    chars = list('Hello World')
    print(letters, matrix, zeros, combined, numbers, chars)


# --accessing items
def accessing_items():
    letters = ['a', 'b', 'c']
    letters[0] = 'A'
    print(letters)


def accessing_items2():
    numbers = list(range(20))
    print(numbers[::2])
    print(numbers[::-2])


# unpacking
def list_unpacking():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    first, second, *other = numbers
    print(first, second, other)


# loop lists
def loop_lists():
    letters = ['a', 'b', 'c']
    for index, letter in enumerate(letters):
        print(index, letter)
# enumerate():return a tuple, read only


# add and remove
def add_remove():
    letters = ['a', 'b', 'c']
    # add
    letters.append('d')
    letters.insert(0, '-')
    # remove
    letters.pop(0)
    letters.remove('b')  # only first 'b'
    del letters[0:3]    # del or delete statement
    letters.clear()  # remove all
    print(letters)


# find
def find():
    letters = ['a', 'b', 'c']
    print(letters.index('a'))  # will return 0
    print(letters.index('d'))  # will get error, use if to aviod
    print(letters.count('d'))


# sort
def sort():
    numbers = [3, 51, 2, 8, 6]
    #numbers.sort(reverse = True)
    print(sorted(numbers, reverse=True))
    print(numbers)


# sort
items = [
    ('p1', 10),
    ('p2', 9),
    ('p3', 22)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# lambda
# sort
items = [
    ('p1', 10),
    ('p2', 9),
    ('p3', 22)
]


items.sort(key=lambda item: item[1])
print(items)
