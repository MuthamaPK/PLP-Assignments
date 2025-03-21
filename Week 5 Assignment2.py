# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # Abstract move method

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road!"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying through the skies!"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on the water!"

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling down the path!"

# Testing the polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for vehicle in vehicles:
        print(vehicle.move())
