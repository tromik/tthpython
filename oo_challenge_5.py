# First, create a class named RaceCar. In the __init__ for the class,
# take arguments for color and fuel_remaining. Be sure to set these
# as attributes on the instance.
# Also, use setattr to take any other keyword arguments that come in.

# OK, now let's add a method named run_lap. It'll take a length argument.
# It should reduce the fuel_remaining attribute by length multiplied by 0.125.
# Oh, and add a laps attribute to the class, set to 0, and increment it each
# time the run_lap method is called.

In Python, attributes defined on the class, but not an instance, are universal.
So if you change the value of the attribute, any instance that doesn't have it
set explicitly will have its value changed, too!
For example, right now, if we made a RaceCar instance named red_car,
then did RaceCar.laps = 10, red_car.laps would be 10!
To prevent this, be sure to set the laps attribute inside of your __init__ method
(it doesn't have to be a keyword argument, though). If you already did it,
just hit that "run" button and you're good to go!


class RaceCar:

    def __init__(self, color, fuel_remaining, laps=0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining = self.fuel_remaining - (length * 0.125)
        self.laps += 1

car = RaceCar(color='red', fuel_remaining=100)
car.run_lap(150)
print("Car has {fuel_remaining} fuel remaining and has ran {laps} laps." \
                .format(fuel_remaining=car.fuel_remaining, laps=car.laps))
car.run_lap(200)
print("Car has {fuel_remaining} fuel remaining and has ran {laps} laps." \
                .format(fuel_remaining=car.fuel_remaining, laps=car.laps))
car.run_lap(350)
print("Car has {fuel_remaining} fuel remaining and has ran {laps} laps." \
                .format(fuel_remaining=car.fuel_remaining, laps=car.laps))
