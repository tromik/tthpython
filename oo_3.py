import random

class Thief:
    sneaky = True
    # methods in classes are actions that the instances of classes can perform
    # methods always take at least one param which is the instance of the class
    # that is calling the method
    # "self" is a convention, but any term could be used

    def __init__(self, name, sneaky=True, **kwargs):
        # __init__ method is not required but gives you more control over
        # instance creation
        self.name = name
        self.sneaky = sneaky

        # assign the kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
            # setattr(x, 'foobar', 123) is equivalent to x.foobar = 123
            # The setattr function takes three arguments:
            # -  the object instance to work on (self)
            # -  the attribute name to define (key)
            # -  the value to give that attribute (value)
            # this could also be done with self.__dict__.update(kwargs)
            # Usually, though, you don't want to update .__dict__ directly as
            # it's mostly meant to be a read-only resource.

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10

tom = Thief(name='Tom')
print("The thief's name: {}".format(tom.name))
print("Is {} sneaky? {}".format(tom.name, tom.sneaky))

jim = Thief(name='Jim', level=6, xp=680, weapon='sword')
print("{name} the thief is level {level} with {xp} XP. {name}'s \
current weapon is a {weapon}." \
        .format(name=jim.name, xp=jim.xp, level=jim.level, weapon=jim.weapon))
