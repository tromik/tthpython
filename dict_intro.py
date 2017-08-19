def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

sep()
# literal construction method of a dictionary
course = {"title": "Python Collections"}

print("The course dictionary: {}".format(course))

print("The course dictionary values: {}".format(course['title']))

sep()
# dict function construction method. Note the double-list
instructors = dict([["name", "Kenneth Love"]])
print("The instructors dictionary: {}".format(instructors))
# the literal construction method of a dictionary is more convenient

sep()
# dictionary with multiple keys (key-value pairs)
# key-value pairs are comma separated
course = {"title": "Python Collections", "teacher": "Kenneth Love", "videos": 22}
print("The course dictionary: {}".format(course))
print("The course dictionary videos value: {}".format(course['videos']))

# trying to retrieve a value of a key that doesn't exist:
# print("The course dictionary 'sample' value: {}".format(course['sample']))
# returns:
# Traceback (most recent call last):
#   File ".\dict_intro.py", line 21, in <module>
#     print("The course dictionary 'sample' value: {}".format(course['sample']))
# KeyError: 'sample'
#
# this is similar to a list's index error

sep()
# handling a key error
try:
    print("The course dictionary 'sample' value: {}".format(course['sample']))
except KeyError:
    print("The key 'sample' does not exist in the course dictionary: {}".format(course))
# returns The key 'sample' does not exist in the course dictionary:
# {'teacher': 'Kenneth Love', 'title': 'Python Collections', 'videos': 22}

sep()
# nested dictionary, teacher is now a dictionary containing first and last name
course = {"title": "Python Collections", "teacher": {"first_name": "Kenneth", "last_name": "Love"}, "videos": 22}
print("The course dictionary with a nested teacher dictionary: {}".format(course))
print("The teacher dictionary from the course dictionary: {}".format(course["teacher"]))
print("The first name value from teacher dictionary from the course dictionary: {}".format(course["teacher"]["first_name"]))

sep()
# Make a dictionary named player and add two keys to it.
# The first key should be "name" and the value can be any string you want.
# The second key should be "remaining_lives". Set this key's value to 3.
player = {"name": "Mario", "remaining_lives": 3}
print("The player dictionary: {}".format(player))

# Now add a "levels" key. It should be a list with the values 1, 2, 3, and 4 in it.
# And, lastly, add an "items" key. This key's value should be another dictionary.
# Give it at least one key and value, but they can be anything you want.
player = {"name": "Mario", "remaining_lives": 3, "levels": [1, 2, 3, 4],
"items": {"sword": "katana", "armor": "leather"}, "state": "big"}
print("The player dictionary: {}".format(player))
