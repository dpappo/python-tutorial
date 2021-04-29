"This is a docstring"

# how do objects, classes, and inheritance work in Python?
# here's a list of functions that are part of every number object
# print(dir(5))

# looking at one of the magic methods aka dunder aka double underscore
print(bool(0))

# classes are the blueprints for objects in python
print(type('a'))
print(type(1))
print(type(True))

# classes are built in and can also be defined, like this:


class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroooooom!")
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print("Halting")


# now let's create an instance of this class

car = Car()
car.increase_speed(10)
car.start()
car.increase_speed(40)
# car.stop()

# objects have built in id methods
print(id(car))

# if we make a new object/instance, it will have a different ID
car2 = Car()
print(id(car2))

# it has unique properties
print(car.speed)
print(car2.speed)
