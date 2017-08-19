# INSTRUCTIONS
# ------------
#
# Let's test unpacking dictionaries in keyword arguments.
# You've used the string .format() method before to fill in blank placeholders.
# If you give the placeholder a name, though, like in template below, you fill it
# in through keyword arguments to .format(), like this:
#     template.format(name="Kenneth", food="tacos")
# Write a function named string_factory that accepts a list of dictionaries as an
# argument. Return a new list of strings made by using ** for each dictionary in
# the list and the template string provided.
#
# Example:
# values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
# string_factory(values)
# ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]
# template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dict_list):
    str_list = []
    for dict in dict_list:
        print("Hi, I'm {name} and I love to eat {food}!".format(**dict))
        str_list.append("Hi, I'm {name} and I love to eat {food}!".format(**dict))
    return str_list

dict_list =  [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]

string_factory(dict_list)
