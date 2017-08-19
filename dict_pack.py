def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

sep()

# dictionary packing and unpacking -> compressing and uncompressing variables

# video notes
# Unpacking a dictionary - Pulling multiple keys and their values of out of a
#     dictionary to feed them to a function.
# >>> my_dict = {'name': 'Kenneth'}
# >>> "Hi, my name is {name}!".format(**my_dict)
# "Hi, my name is Kenneth!"
#
# Packing a dictionary - Putting multiple keyword arguments into a single dictionary.
#
# >>> def packing(**kwargs):
# ...     print(len(kwargs))
# >>> packing(name="Kenneth")
# 1

tom = {"first_name": "Tom", "job": "Developer"}
print("My dictionary: {}".format(tom))
