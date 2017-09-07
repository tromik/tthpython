from characters import Character
from thieves import Thief

"""
isinstance(<object>, <class>)
    This function will tell you whether or not <object> is an instance of <class>.
    If it could be an instance of several classes, you can use a tuple of classes like so:
        isinstance(<object>, (<class1>, <class2>, <class3>)).
issubclass(<class>, <class>)
    This function will tell you whether or not one class is a descendent of another class.
    Just like isinstance(), you can use a tuple of classes to compare against.
type(<instance>)
    will give you the class for an instance, as will instance.__class__.
    Neither of these is particularly useful.
"""
tom = Thief(name="Tom")

print("Is Tom a Thief? {}".format(isinstance(tom, Thief))) # True
print("Is Tom a Character? {}".format(isinstance(tom, Character))) # True

print("Is a thief a character? {}".format(issubclass(Thief, Character))) # True
print("Is a character a thief? {}".format(issubclass(Character, Thief))) # False

print("What is tom? {}".format(type(tom)))

print("What is tom in a nicer format? {}".format(tom.__class__.__name__))

lineage = []
for x in tom.__class__.__mro__:
    lineage.append(x.__name__)
print("What is tom's lineage? {}".format(lineage))
