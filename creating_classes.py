"""Practice1: Implement inheritance and customization in transportation classes.
"""


class Transport:
    """ Represents a mode of transportation.
    Attributes:
        name (str): The name of the transport.
        capacity (int): The passenger capacity of the transport.
        max_speed (float): The maximum speed of the transport in kilometers per hour (km/h).
    """

    def __init__(self, name, capacity, max_speed):
        """Initialize a new Transport object."""
        self.name = name
        self.capacity = capacity
        self.max_speed = max_speed

    def travel(self, distance):
        """Simulate traveling a certain distance."""
        print(f"{self.name} is traveling {distance} km.")

    def show_info(self):
        """Show information about the transport."""
        print(f"Name: {self.name}")
        print(f"Capacity: {self.capacity}")
        print(f"Max Speed: {self.max_speed} km/h")


class Car(Transport):
    """
    Represents a car, a type of transport vehicle.

    Attributes:
        name (str): The name of the car.
        capacity (int): The passenger capacity of the car.
        max_speed (float): The maximum speed of the car in kilometers per hour (km/h).
        num_doors (int): The number of doors the car has.
    """

    def __init__(self, name, capacity, max_speed, num_doors):
        """Initialize a new Car object."""
        super().__init__(name, capacity, max_speed)
        self.num_doors = num_doors

    def travel(self, distance):
        """Simulate driving a certain distance."""
        print(f"{self.name} is driving {distance} km.")

    def show_info(self):
        """Show information about the car."""
        super().show_info()
        print(f"Number of Doors: {self.num_doors}")

    @staticmethod
    def honk_horn():
        """Method to honk the horn."""
        print("Beep! Beep!")


# Bicycle class inheriting from Transport
class Bicycle(Transport):
    """
    Represents a bicycle, a type of transport.

    Attributes:
        name (str): The name of the bicycle.
        capacity (int): The passenger capacity of the bicycle.
        max_speed (float): The maximum speed of the bicycle in kilometers per hour (km/h).
        num_wheels (int): The number of wheels the bicycle has.
    """

    def __init__(self, name, capacity, max_speed, num_wheels):
        """Initialize a new Bicycle object."""
        super().__init__(name, capacity, max_speed)
        self.num_wheels = num_wheels

    def travel(self, distance):
        """Simulate riding a certain distance."""
        print(f"{self.name} is riding {distance} km.")

    def show_info(self):
        """Show information about the bicycle."""
        super().show_info()
        print(f"Number of Wheels: {self.num_wheels}")

    @staticmethod
    def ring_bell():
        """Method to ring the bell."""
        print("Ring! Ring!")


# Bus class inheriting from Transport
class Bus(Transport):
    """
    Represents a bus, a type of transport.

    Attributes:
        name (str): The name of the bus.
        capacity (int): The passenger capacity of the bus.
        max_speed (float): The maximum speed of the bus in kilometers per hour (km/h).
        num_floors (int): The number of floors the bus has.
    """

    def __init__(self, name, capacity, max_speed, num_floors):
        """Initialize a new Bus object."""
        super().__init__(name, capacity, max_speed)
        self.num_floors = num_floors

    def travel(self, distance):
        """Simulate driving a certain distance."""
        print(f"{self.name} is driving {distance} km.")

    def show_info(self):
        """Show information about the bus."""
        super().show_info()
        print(f"Number of Floors: {self.num_floors}")

    @staticmethod
    def announce_stop():
        """Method to announce stops."""
        print("Next stop, please prepare to alight.")


# Boat class inheriting from Transport
class Boat(Transport):
    """
    Represents a boat, a type of transport.

    Attributes:
        name (str): The name of the boat.
        capacity (int): The passenger capacity of the boat.
        max_speed (float): The maximum speed of the boat in kilometers per hour (km/h).
        propulsion_type (str): The type of propulsion used by the boat.
    """

    def __init__(self, name, capacity, max_speed, propulsion_type):
        """Initialize a new Boat object."""
        super().__init__(name, capacity, max_speed)
        self.propulsion_type = propulsion_type

    def travel(self, distance):
        """Simulate sailing a certain distance."""
        print(f"{self.name} is sailing {distance} nautical km.")

    def show_info(self):
        """Show information about the boat."""
        super().show_info()
        print(f"Propulsion Type: {self.propulsion_type}")

    @staticmethod
    def set_sail():
        """Method to set sail."""
        print("Hoist the sails! We're setting sail.")


if __name__ == "__main__":
    # Creating instances of the Transport subclasses
    car = Car("Toyota", 5, 120, 4)
    bicycle = Bicycle("Giant", 1, 20, 2)
    bus = Bus("CityExpress", 50, 60, 2)
    boat = Boat("Sailor", 10, 30, "Wind")

    # Invoking methods on each instance
    print("------ Car ------")
    car.travel(50)
    car.show_info()
    car.honk_horn()

    print("\n------ Bus ------")
    bus.travel(100)
    bus.show_info()
    bus.announce_stop()

    print("\n------ Bicycle ------")
    bicycle.travel(10)
    bicycle.show_info()
    bicycle.ring_bell()

    print("\n------ Boat ------")
    boat.travel(20)
    boat.show_info()
    boat.set_sail()
