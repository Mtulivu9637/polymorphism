# Polymorphism Example with Vehicles and Animals

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

class Dog:
    def move(self):
        print("Running 🐕")

class Bird:
    def move(self):
        print("Soaring 🦅")


# List of different objects
things = [Car(), Plane(), Boat(), Dog(), Bird()]

# Polymorphism: same method name, different behaviors
for thing in things:
    thing.move()
