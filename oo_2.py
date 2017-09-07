import random

class Thief:
    sneaky = True
    # methods in classes are actions that the instances of classes can perform
    # methods always take at least one param which is the instance of the class
    # that is calling the method
    # "self" is a convention, but any term could be used

    def pickpocket(self):
        # print("Called by {}".format(self))
        if self.sneaky:
            return bool(random.randint(0, 1))
        else:
            return False

    def hide(self, light_level):
        return self.sneaky and light_level < 10

tom = Thief()
pickpocket_outcome = tom.pickpocket() # note that no input params are needed, self
                                      # is passed in by default as the instance
print("Tom's pickpocket successful? {}".format(pickpocket_outcome))

# what is essentially happening with the self param in the method is this:
result = Thief.pickpocket(tom)
print("Manually passing the instance into the method, result is a: {}".format(result))

tom.sneaky = False
print("Tom's pickpocket successful? {}".format(tom.pickpocket()))
print("Tom's pickpocket successful? {}".format(tom.pickpocket()))
print("Tom's pickpocket successful? {}".format(tom.pickpocket()))
print("Tom's pickpocket successful? {}".format(tom.pickpocket()))
print("Tom's pickpocket successful? {}".format(tom.pickpocket()))

tom.sneaky = True

print("Can Tom hide? {}".format(tom.hide(4)))
