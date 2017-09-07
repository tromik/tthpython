class Character:
    def __init__(self, name='', **kwargs):
        # without a default on name, an exception will occur:
        # TypeError: __init__() missing 1 required positional argument: 'name'
        # this is explicit
        # now that name has a default value of an empry string, we need to
        # validate it ourself
        if not name:
            raise ValueError("'name' is required")

        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        # see https://docs.python.org/3/reference/datamodel.html#special-method-names
        return "{class_name}: {object_name}".format(class_name=self.__class__.__name__,
                                                    object_name=self.name)
