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
        # return self.value  + str(other)
        # ^ not very helpful or useful
        # if "." in self.value:
        #     return float(self.value) + other
        # return int(self.value) + other
        # now NumString objects support mathematical additional
        # this also works (no value)
        if "." in self.value:
            return float(self) + other
        return int(self) + other
        # this will only work when the NumString is on the LEFT of the equation
        # __radd__ (reflect add) needed for other

    def __radd__(self, other):
        # if "." in self.value:
        #     return other + float(self)
        # return other + int(self)
        # now NumString(5) + 4 and 4 + NumString(5) will work
        # However, can also do this:
        return self + other
        # which will call __add_
        # 4 + NumString(5) -- > __add__, fails, passed to __radd__ reflected which
        #   uses __add__

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
