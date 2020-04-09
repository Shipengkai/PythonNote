values2 = [x * 2 for x in range(5)]  # list
values3 = {x * 2 for x in range(5)}  # set
values4 = {}  # dictionary
for x in range(5):
    values4[x] = x * 2
print('list: ', values2, '\n', 'set: ', values3, '\n', 'dictionary: ', values4)

values = {x: x*2 for x in range(5)}
print('dictionary: ', values)
