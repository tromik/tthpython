from thieves import Thief

tom = Thief(name="Tom", sneaky=False)
# name is now a keyword so that it is not simply positional in the init
print("{name} sneaky? {sneaky}".format(name=tom.name, sneaky=tom.sneaky))
print("{name} agile? {agile}".format(name=tom.name, agile=tom.agile))
print("{name} hide? {hide}".format(name=tom.name, hide=tom.hide(8)))

# john=Thief(sneaky=True)
# this will cause this exception
#   ValueError: 'name' is required
# from Character init

# inspect.getmro() or class.__mro__ can be used to a class's method
# resolution order (MRO)
print(Thief.__mro__)
# (<class 'thieves.Thief'>, <class 'attributes.Agile'>,
# <class 'attributes.Sneaky'>, <class 'characters.Character'>, <class 'object'>)

print(tom)  # running print on tom before the Character class was modified
            # returns <thieves.Thief object at 0x00A8E1D0>
# after updating the Character class, when print is called on tom, it
# returns Thief: Tom
print(repr(tom))    # running this returns <thieves.Thief object at 0x00A8E1D0>
                    # which is what print(tom) did previously
                    # this can also be overridden with __repr__
