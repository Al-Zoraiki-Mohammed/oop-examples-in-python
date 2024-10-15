"""Implement multiple inheritance with abstract classes and magic methods.
"""

from abc import ABC, abstractmethod


class AbstractTransport(ABC):
    """Abstract base class representing a mode of transportation."""

    def __init__(self, name):
        """Initialize a new AbstractTransport object with a name."""
        self.name = name

    @abstractmethod
    def travel(self):
        """Abstract method to simulate travel."""

    @abstractmethod
    def show_info(self):
        """Abstract method to display information about the transport."""

    def __add__(self, other):
        """Concatenate the names of two transports."""
        return f"{self.name} joined with {other.name}"

    def __sub__(self, other):
        """Create a string indicating separation between two transports."""
        return f"{self.name} separated from {other.name}"

    def __eq__(self, other):
        """Check if two transports have the same name."""
        return self.name == other.name

    def __lt__(self, other):
        """Compare the lengths of the names of two transports."""
        return len(self.name) < len(other.name)

    def __len__(self):
        """Get the length of the name of the transport."""
        return len(self.name)

    def __getitem__(self, index):
        """Get the character at the specified index in the name."""
        return self.name[index]

    @staticmethod
    def hello():
        """Static method to greet from AbstractTransport."""
        return "Hello from AbstractTransport"

    @classmethod
    def from_str(cls, name_str):
        """Alternate constructor to create an instance from a string."""
        name = name_str.split()[0]
        return cls(name)

    @property
    def name_length(self):
        """Property to get the length of the name."""
        return len(self.name)


class Engine:
    """Class representing an engine with fuel type."""

    def __init__(self, fuel_type):
        """Initialize a new Engine object with a fuel type."""
        self.fuel_type = fuel_type

    @staticmethod
    def start():
        """Method to start the engine."""
        return "Engine started."

    @staticmethod
    def stop():
        """Method to stop the engine."""
        return "Engine stopped."


class Transport(AbstractTransport, Engine):
    """Class representing a mode of transportation with an engine."""

    def __init__(self, name, fuel_type):
        """Initialize a new Transport object with a name and fuel type."""
        AbstractTransport.__init__(self, name)
        Engine.__init__(self, fuel_type)

    def travel(self):
        """Method to simulate travel."""
        return f"{self.name} is traveling."

    def show_info(self):
        """Method to display information about the transport."""
        return f"Name: {self.name}, Fuel Type: {self.fuel_type}"


class Car(Transport):
    """Class representing a car as a mode of transportation."""

    def __init__(self, name, fuel_type, num_doors):
        """Initialize a new Car object with a name, fuel type, and number of doors."""
        super().__init__(name, fuel_type)
        self.num_doors = num_doors

    def open_door(self):
        """Method to open a door of the car."""
        return f"{self.name} opens door."

    def travel(self):
        """Override travel method to simulate driving."""
        return f"{self.name} is driving."


if __name__ == "__main__":
    print('--' * 10 + 'Object1' + '--' * 10)
    car1 = Car("Honda", "Petrol", 5)
    print(car1.travel())
    print(car1.show_info())
    print(car1.start())
    print(car1.open_door())
    print(car1.hello())
    print(car1.name_length)

    print('--' * 10 + 'Object2' + '--' * 10)

    car2 = Car("Toyota", "Gasoline", 4)
    print(car2.travel())
    print(car2.show_info())
    print(car2.start())
    print(car2.open_door())
    print(car2.hello())
    print(car2.name_length)
