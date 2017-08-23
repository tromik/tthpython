# Alright, this one might be a bit challenging but you've been doing great so far,
# so I'm sure you can manage it.
# I need you to make a function named word_count. It should accept a single argument
# which will be a string. The function needs to return a dictionary. The keys in
# the dictionary will be each of the words in the string, lowercased. The values
# will be how many times that particular word appears in the string.
# Check the comments below for an example.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

# def word_count(val):
#     str_list = val.lower().split(" ")
#     str_dict = {}
#     for word in str_list:
#         cnt = 0
#         for cnt_word in str_list:
#             if word == cnt_word:
#                 cnt += 1
#                 str_dict.update({word: cnt})
#     return str_dict

# def wtf():
#     t = [1,2,3,4,5]
#     for e in t:
#         print(e)
#         print("Going into inner")
#         for e_two in t:
#             print(e_two)
#         print("Done inner")

# word_count("blah hi I am a Tom blah my name is Tom I know")
#
# print(wtf())
# print("-------")

def word_count(val):
    val = val.lower().split()
    result = {}

    for word in val:
        if word in result:
            result[word] =  result[word] + 1
            continue
        result[word] = 1

    return result

print(word_count("I do not like it Sam I Am"))

print(word_count("AM AM AM WITH WITH TOM TOM TOM TOM HI"))

print(word_count("55555 55555 55555 55555 55555 22 22 1"))
