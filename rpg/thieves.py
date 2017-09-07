import random

from attributes import Agile, Sneaky
from characters import Character


class Thief(Agile, Sneaky, Character):
    # mro - method resolution order
    # Method Resolution Order (MRO) controls the order that classes are
    # searched through to find a particular method.
    # in this case we want the Character to be the last class initialized
    # as it is top level and has no super
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
