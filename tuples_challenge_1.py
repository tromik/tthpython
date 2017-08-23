# Create a function named multiply that takes any number of arguments. Return the
# product (multiplied value) of all of the supplied arguments.
# The type of argument shouldn't matter.
# Slices might come in handy for this one.

def multiply(*args):
    product = 1
    try:
        for num in args:
            product = product * num
    except ValueError:
        print("Bad args")
    else:
        return product

print(multiply(1, 2, 2, 4, 2, 1))
