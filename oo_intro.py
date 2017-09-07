class Thief:
    # pass
    # use pass to create an empty class that can be filled in later
    # variables in a class are attributes
    sneaky = True

tom = Thief() # instance
print("Tom's sneaky: {}".format(tom.sneaky))
print("Class' sneaky: {}".format(Thief.sneaky))

# instances are responsible for their own attribute values
tom.sneaky = False
print("Tom's sneaky after update: {}".format(tom.sneaky))
print("Class' sneaky: {}".format(Thief.sneaky))

# use del to delete instances
del tom
