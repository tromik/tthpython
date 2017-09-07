instructions = """
Let's use __str__ to turn Python code into Morse code!
OK, not really, but we can turn class instances into a representation of their
Morse code counterparts.

I want you to add a __str__ method to the Letter class that loops through the
pattern attribute of an instance and returns "dot" for every "." (period) and
"dash" for every "_" (underscore). Join them with a hyphen.

I've included an S class as an example (I'll generate the others when I test
your code) and it's __str__ output should be "dot-dot-dot".
"""

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse_code = []
        for char in self.pattern:
            if char == ".":
                morse_code.append("dot")
            elif char == "_":
                morse_code.append("dash")
        return "-".join(morse_code)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)
