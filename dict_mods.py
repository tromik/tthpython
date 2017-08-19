def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

sep()

tom = {"first_name": "Tom", "job": "Developer"}
print("My dictionary: {}".format(tom))

sep()
# adding a new key is done the same way as updating, where the key does not exist
# only one key can be changed at a time using this method
tom["last_name"] = "Ross"
print("My dictionary with my last name: {}".format(tom))

sep()
# dictionaries are mutable and can be changed in place using functions that allow
# for multiple keys to be added or changed at the same time
# using the update function to update first name and add editor:
tom.update({"first_name": "Thomas", "editor": "Atom"})
print("My dictionary with my changed first name and editor: {}".format(tom))

sep()
# cannot add two dictionaries together as Python wouldn't know which to
# prioritize if they had the same key name
try:
    tom_test = {"first_name": "Tom"} + {"last_name": "Ross"}
except TypeError: # adding two dictionaries throws a type error
    # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
    print("Cannot add dictionaries together.")
# prints Cannot add diction together.

sep()
# changing a single value of an existing key can be done the same way as adding
# one new key:
tom["editor"] = "Any"
print("My dictionary with new editor: {}".format(tom))

sep()
# Removing a key from a dictionary can be done with the del command:
del tom["job"]
print("My dictionary without job: {}".format(tom))

# notes:
# .pop(<key>) - like lists, dicts have .pop(). It'll return the key's value to you
#     and then delete the key.
# .popitem() - similar to .pop() but instead of returning just the value, returns
#     you a tuple (more in the next stage!) with the key and the value. Also, this
#     doesn't take any arguments, you get a random key/value pair!
# .clear() - need to quickly empty out a dictionary? This method is your
#     tool of choice, then.
