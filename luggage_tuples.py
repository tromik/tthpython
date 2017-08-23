def sep():
    print("-" * 160)
    print("")
    print("-" * 160)


def packer(**kwargs):
    print(kwargs)
    # prints a dictionary where the key is the argument name and the value is
    # argument value

def packer_over(name="Tom", lang="English", **kwargs):
    print(kwargs)
    # prints a dictionary where the key is the argument name and the value is
    # argument value
    # This time the name key is defaulted so it is removed from kwargs
    if kwargs["num"] == 42:
        print("42 is the answer.")
    # to access a key in kwargs treat it like a dictionary

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

sep()
packer(name="Kenneth", num=42, spanish_inquisition=None)
# returns {'spanish_inquisition': None, 'name': 'Kenneth', 'num': 42}

packer_over(name="Kenneth", num=42, spanish_inquisition=None)
# returns {'spanish_inquisition': None, 'num': 42}
# name was set to None effectively removing it from the dict

sep()
unpacker(**{"first_name": "Kenneth", "last_name": "Love"})
# prints Hi Kenneth Love!
# unpacking turns a dictionary into an argument key value pairs

sep()
#tuple work starts here
course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))

sep()
# enumerate creates tuples in pairs where the first value is the
# index and the second value is the value from the list
enum = "abc" # string is an ordered iterable like a list
sets = enumerate(enum)
print(sets)
# returns <enumerate object at 0x035C8558>
# use list function to return as a list of tuples
print(list(sets))
# reutns [(0, 'a'), (1, 'b'), (2, 'c')]
# alternatively, use the dict() function to return a dictionary of key-value pairs
print(dict(enumerate(enum)))
# returns {0: 'a', 1: 'b', 2: 'c'}
