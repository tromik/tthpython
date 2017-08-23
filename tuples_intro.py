def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

# tuples are another type of collection
# they are immutable, which means you cannot change them in place
# changing a tuple will create a new one and the original will be retained

# constructing
my_tuple = (1, 2, 3)
# the commas between the values denote the tuple during construction, not the
# parathesis
print(my_tuple)
# returns (1, 2, 3)

my_second_tuple = 1, 2, 3
print(my_second_tuple)
# still returns (1, 2, 3)
sep()
# because the commas denote the tuple during construction, they are required
# even when creating an item with one value

my_third_tuple = (5)
print(my_third_tuple)
# returns 5, a single bit int
my_third_tuple = (5, )
print(my_third_tuple)
# returns (5, ), a tuple
sep()
# the tuple function can also be used to create a tuple by passing in a list
my_fourth_tuple = tuple([1, 2, 3])
print(my_fourth_tuple)
# returns (1, 2, 3)
sep()
# tuples are immutable
# my_tuple[0] = 5
# TypeError: 'tuple' object does not support item assignment

try:
    my_tuple[0] = 5
except TypeError:
    print("Tuples are immutable")

tuple_with_list = (1, "apple", [1, 2, 3])

try:
    tuple_with_list[0] = 5
except TypeError:
    print("Tuples are immutable")

try:
    tuple_with_list[1] = "banana"
except TypeError:
    print("Strings and tuples are immutable")

try:
    tuple_with_list[2][1] = 5 # this does work, the list in the tuple is mutable
except TypeError:
    print("Tuples are immutable")
else:
    print(tuple_with_list)
# this means that while tuples are immutable the mutable items within a tuple
# can be changed
