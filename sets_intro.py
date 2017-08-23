def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

# old way of creating a set required the use of the set function
my_set = set([1, 2, 3])
print(my_set)

# in Python3 you can use curly braces alone to create a set if the set is not empty
new_set = {1, 2, 3} # note that while it uses curly braces, it is not structured
                    # in key value pairs like a dictionary
print(new_set)

# however, if the set is empty Python will create a dictionary
maybe_set = {}
print(type(maybe_set)) # --> dict

# to create an empty set, use the set function
yes_set = set({})
print(type(yes_set)) # --> set

sep()
# sets do not have an index or a defined order
num_set = {1, 11, 13, 7, 5, 3}
print("num_set : {}".format(num_set)) # --> num_set : {1, 3, 5, 7, 11, 13}
# python will attempt to order but it is not defined

sep()
# adding to a set, single element
low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17)
print("low_primes: {}".format(low_primes)) # --> low_primes: {1, 3, 5, 7, 11, 13, 17}
# sets are mutable and are updated in place, like a list

sep()
# adding to a set, multiple elements, sets added to sets
low_primes = {1, 3, 5, 7, 11, 13}
low_primes.update({17, 19, 23}, {2, 29})    # multiple elements and multiple sets
                                            # being added at once
print("updated low primes: {}".format(low_primes)) # --> updated low primes: {1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

sep()
# removing elements from sets
low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(15)
print("low_primes with 15: {}".format(low_primes)) # --> low_primes with 15: {1, 3, 5, 7, 11, 13, 15}
low_primes.remove(15)
print("low_primes without 15: {}".format(low_primes)) # --> low_primes without 15: {1, 3, 5, 7, 11, 13}

# trying to remove() something that doesn't exist will cause a KeyError
test = 101
try:
    low_primes.remove(test)
except KeyError:
    print("Value {} does not exist in {}".format(test, low_primes))
# --> Value 101 does not exist in {1, 3, 5, 7, 11, 13}

# however, using discard will not throw an error if the element does not exist
# if it does exist it will be removed
test = 104
try:
    low_primes.discard(test)
    print("{} did not exist in {} but no error".format(test, low_primes))
except:
    print("Value {} does not exist in {}".format(test, low_primes))
# --> 104 did not exist in {1, 3, 5, 7, 11, 13} but no error

# you can also pop items off of sets
while low_primes:
    print(low_primes.pop())
