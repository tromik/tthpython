class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        # five = 5
        # five + 4 = '54'
        return self.value  + str(other)

# >>> from numstring import NumString
# >>> five = NumString(5)
# >>> five
# <numstring.NumString object at 0x0031E210>
# >>> print(5)
# 5
# >>> str(5)
# '5'
# >>> int(5)
# 5
# >>> float(5)
# 5.0
# >>>
