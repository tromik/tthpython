# I need you to add a method name praise. The method should return a positive
# message about the student which includes the name attribute. As an example,
# it could say "You're doing a great job, Jacinta!" or
# "I really like your hair today, Michael!".
# Feel free to change the name attribute to your own name, too!

class Student:
    name = "Your Name"

    def praise(self):
        print("Nice work, {}".format(self.name))

tom = Student()
tom.name = 'Tom'

tom.praise()
