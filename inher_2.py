import random

class Character:

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Thief(Character):
    # class Thief inherits from class Character, making Thief a subclass or child
    # of the parent or super class Character
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        # override the __init__ function from the superclass
        super().__init__(name, **kwargs) # where the super is called matters
        # name assignment will take place here
        # sneaky is set after the super's __init__ is used in this case
        self.sneaky = sneaky
        # subclasses can take different arguments that the super class

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10

tom = Thief('Tom', sneaky=False, weapon='sword')
# tom is both a Thief and a Character, name for Thief comes from Character
print("Is {name} sneaky? {sneaky}".format(name=tom.name, sneaky=tom.sneaky))
print("{name}'s weapon is a {weapon}".format(name=tom.name, weapon=tom.weapon))
