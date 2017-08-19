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
