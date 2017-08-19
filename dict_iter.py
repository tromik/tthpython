def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

# video notes
# -----------
# >>> my_dict = {'a': 1, 'b': 2, 'c': 3}
# >>> for key in my_dict:
# . . .     print(key)
# a
# b
# c

# New Terms
# * `.keys()` - this method returns an iterable of all of the keys
# in a dictionary.
# * `.values()` - this method returns an iterable of all of the values
# in the dictionary.
# * `.items()` - this method is basically a combo of the above two. It returns an
# iterable of key/value pairs inside of tuples (more on them in the next stage!).

sep()
course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": "133"}

for course in course_minutes:
    print(course)
# Prints the keys in the dictionary only
# Python Basics
# Flask Basics
# Django Basics
# Java Basics

sep()
for course in course_minutes:
    print(course_minutes[course])
# prints only the values in the dictionary:
# 133
# 232
# 237
# 189
# not very useful data without the related keys

sep()
for key in course_minutes.keys():
    print(key)

sep()
for value in course_minutes.values():
    print(value)
# These perform the same actions as the loops above but using the keys and values functions

sep()
for item in course_minutes.items():
    print(item)
# items() returns tuples:
# ('Django Basics', 237)
# ('Flask Basics', 189)
# ('Python Basics', 232)
# ('Java Basics', '133')

sep()
def unpacker(name=None, minutes=None):
    if name and minutes:
        print("Hi {} {}!".format(name, minutes))
    else:
        print("Hi no time course!")

def packer(test="Bleh", **kwargs):
    print(kwargs)

for item in course_minutes.items():
    unpacker(**item)
