# built in primitive types in python:numbers, booleans, strings.
"""
student_count = 1000
rating = 4.99
is_published = False
course_name = "python programming"
#four things
"""
# 1 all my variable names are descriptive and meaningful
# 2 use lower case letters to name my variables
# 3 use an underscore to separate multiple words
# 4 put a space around the equals sign


# string:
course_name = "Python Programming"
# len()
print(len(course_name))
# get a character
print(course_name[0])
print(course_name[-1])
# slice a string
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])


# escape character: \(backslash)
# escape sequence: \"
print("Python \nProgramming")
# \\ : \
# \n : a new line


# formatted string:
first = "teri"
last = "teriri"
full1 = first + " " + last
full2 = f"{first} {last}"
print(f"full1:{full1}\nfull2:{full2}")


# string functions:
course = "python  py   "
print(course.upper())  # return a new string
print(course.lower())
print(course.title())
print(course.strip())  # remove white space l/r
print(course.find('pyt'))
print(course.replace("p", "j"))
print('pro' in course)
print('teriri' not in course)
