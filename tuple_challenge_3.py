# Create a function named combo that takes two ordered iterables.
# These could be tuples, lists, strings, whatever.
# Your function should return a list of tuples. Each tuple should hold the first
# item in each iterable, then the second set, then the third, and so on.
# Assume the iterables will be the same length.
# Check the code below for an example.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(arg1, arg2):
    # return list(zip(arg1, arg2))
    # they wouldn't let me use zip()
    # instead create a list
    # loop through the enumerated first collection arg
    # use the index to get the value from the second collection
    # generate a tuple (x, y)
    # append the tuple to the list
    listy = []
    for index, a in enumerate(arg1):
        tuppy = (a, list(arg2)[index])
        listy.append(tuppy)
    return listy



print(combo([1, 2, 3], 'abc'))
