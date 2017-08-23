def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

sep()

a = 5
b = 20
print("a: {}\tb: {}".format(a, b))
# need a to be 20 and a to be 5 without creating a placeholder variable c
a, b = b, a
print("a: {}\tb: {}".format(a, b))

# tuples do not have key-value pairs like dictionary so each item in the tuple
# unpacks to a single variable

sep()
def add(base, *args):
    total = base
    for num in args:
        total += num
    return total

print(add(5, 3, 2, 1))
# returns 11

# kwargs is always last, args is always second to last
def argkwarg(base, value, *args, **kwargs):
    total = base + value
    for num in args:
        total += num
    return total

sep()
