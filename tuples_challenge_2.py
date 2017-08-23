# Create a function named stringcases that takes a single string but returns a tuple
# of different string formats. The formats should be:
# * All uppercase
# * All lowercase
# * Titlecased (first letter of each word is capitalized)
# * Reversed
# There are str methods for all but the last one.

def stringcases(val):
    uppercase = val.upper()
    lowercase = val.lower()
    titlecase = val.title()

    reversecase = ''
    for char in val[::-1]:
        reversecase += char

    return uppercase, lowercase, titlecase, reversecase



print(stringcases("hello MY naMe is tOM!"))
