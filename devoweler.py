def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        try:
            word = word.replace(vowel, '')
        except ValueError:
            pass
    return word

print(disemvowel('apple'))
print(disemvowel('orange'))
print(disemvowel('soup'))
print(disemvowel('tomross'))
print(disemvowel('sOuP'))
print(disemvowel('tOmROss'))
