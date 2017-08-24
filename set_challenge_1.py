# write a function named covers that accepts a single parameter, a set of topics.
# Have the function return a list of courses from COURSES where the supplied set
# and the course's value (also a set) overlap.
# For example, covers({"Python"}) would return ["Python Basics"].

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    result = []
    for topic in topics:
        for course, covers in COURSES.items():
            for covered_topic in covers:
                if topic == covered_topic:
                    result.append(course)
    return result


print("Result: {}".format(covers({"Python", "Java"})))

# Create a new function named covers_all that takes a single set as an argument.
# Return the names of all of the courses, in a list, where all of the topics in
# the supplied set are covered.
# For example, covers_all({"conditions", "input"}) would return
#       ["Python Basics", "Ruby Basics"].
# Java Basics and PHP Basics would be exclude because they don't include
# both of those topics.

def covers_all(topics):
    result = []
    for course, covers in COURSES.items():
        if topics < covers:
            result.append(course)
    return result

print("Result: {}".format(covers_all({"conditions", "input"})))
