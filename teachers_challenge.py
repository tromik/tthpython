# For this first task, create a function named num_teachers that takes a single
# argument, which will be a dictionary of Treehouse teachers and their courses.
# The num_teachers function should return an integer for how many teachers are
# in the dict.

def num_teachers(val):
    return len(val)

# Create a new function named num_courses that will receive the same dictionary
# as its only argument.
# The function should return the total number of courses for all of the teachers.

def num_courses(val):
    cnt = 0
    for value in val.values():
        cnt = cnt + len(value)
    return cnt

# For this step, make another new function named courses that will, again,
# take the dictionary of teachers and courses.
# courses, though, should return a single list of all of the available courses
# in the dictionary. No teachers, just course names!

# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.

def courses(val):
    course_list = []
    for value in val.values():
        print(value)
        for course in value:
            if course in course_list:
                continue
            else:
                course_list.append(course)
    return course_list

# courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})


# Create a function named most_courses that takes our good ol' teacher dictionary.
# most_courses should return the name of the teacher with the most courses.
# You might need to hold onto some sort of max count variable.

def most_courses(val):
    total_for_teacher = 0
    teacher_with_most = ""
    for key, value in val.items():
        if len(value) > total_for_teacher:
            total_for_teacher = len(value)
            teacher_with_most = key
    return teacher_with_most

# print(most_courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}))

# In this last challenge, I want you to create a function named stats and it'll
# take our teacher dictionary as its only argument.
# stats should return a list of lists where the first item in each inner list is
# the teacher's name and the second item is the number of courses that teacher has.
# For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]

def stats(val):
    stat_list = []
    for key, value in val.items():
        stat_list.append([key, len(value)])
    return stat_list

# print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}))
