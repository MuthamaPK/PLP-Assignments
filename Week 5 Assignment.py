#Assignment 1
class SuperHero:
    def __init__(self, name, power, city, strength_level):
        self.name = name
        self.__power = power  # Private attribute
        self.__city = city    # Private attribute
        self.__strength_level = strength_level  # Private attribute

    def introduce(self):
        return f"I am {self.name}, protecting {self.__city}, with the power of {self.__power}!"

    def save_day(self):
        return f"{self.name} has saved the day using {self.__power}!"

    def get_city(self):
        return self.__city  # Getter for private attribute
    
    def set_city(self, new_city):
        self.__city = new_city  # Setter for private attribute

    def get_power(self):  
        return self.__power  # Getter for private attribute


class FlyingHero(SuperHero):
    def __init__(self, name, power, city, strength_level, flight_speed):
        super().__init__(name, power, city, strength_level)
        self.flight_speed = flight_speed  # New attribute specific to FlyingHero

    def save_day(self):  # Method override
        return f"{self.name} soared at {self.flight_speed} kph to save the day using {self.get_power()}!"


class TechHero(SuperHero):
    def __init__(self, name, power, city, strength_level, gadgets):
        super().__init__(name, power, city, strength_level)
        self.gadgets = gadgets  # New attribute specific to TechHero

    def save_day(self):  # Method override
        gadget_list = ", ".join(self.gadgets)
        return f"{self.name} used gadgets like {gadget_list} to save the day with {self.get_power()}!"


if __name__ == "__main__":
    hero1 = FlyingHero("SkySurge", "Flight", "New York", 500, 1000)
    hero2 = TechHero("TechWhiz", "Intelligence", "Silicon Savanna", 300, ["Drone", "AI Suit"])

    print(hero1.introduce())
    print(hero1.save_day())

    print(hero2.introduce())
    print(hero2.save_day())

#Assignment 2
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
