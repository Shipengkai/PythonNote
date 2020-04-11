# list()
# tuple()
# set()
# dict()
point = dict(x=1, y=2)
#point = {'x': 1, 'y': 2}
print(point['x'])
point['x'] = 10
point['z'] = 20
# get
if 'a' in point:
    print(point['a'])
print(point.get('a', 0))
# delete
del point['x']  # AAAAAAAAAAAAAAAAAAAAA dict删除
print(point)
# loop
for key in point:                       # dict遍历：直接遍历，访问key； .item遍历，访问key，value  AAAAAAAAAAAAAAAAAAAA
    print(key, point[key])
for key, value in point.items():
    print(key, value)
