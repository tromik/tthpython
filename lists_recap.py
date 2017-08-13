things = ['apple', 'banana', 'orange']

# add an item to the list
print(things + ['peach'])
# make the chnage permanent
things += ['peach']
print(things)

# append works pretty much the same way, use to add one item to a list
things.append('tomato') # note no brackets
print(things)

# remove item from list
# last item in a list is index -1
del things[-1]
print(things)

# add multiple items to the end of a list
things.extend(['pineapple', 'pear'])
print(things)
# can also be used to add a non-list to the end of a list if the item is
# iterable
things.extend('abcd')
print(things)

# insert add an item to a list in a specific position/index
del things[1] # remove banana from list
things.insert(1, 'cherry')
print(things)
