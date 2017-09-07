# Alright, I need you make a new method named feedback. It should take an
# argument named grade.
#
# Methods take arguments just like functions do. You'll still need self
# in there, though.
#
# If grade is above 50, return the result of the praise method.
# If it's 50 or below, return the reassurance method's result.

class Student:
    name = "Your Name"

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()

tom = Student()
tom.name = 'Tom'

print(tom.feedback(60))
print(tom.feedback(20))
