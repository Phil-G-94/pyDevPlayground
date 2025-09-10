# OOP with Python

# instantiate a class using the `class` keyword #


# class Pod:
#     pass  # does nothing, indicates class properties will be defined later


# class Person:
#     name: str
#     surname: str


# p = Person()
# p.name = "Jack"
# p.surname = "Delaney"
# print(f"The person's name is {p.name} {p.surname}")

# using `self` - equivalent to `this` in JavaScript
# the __init__ method is run as soon as
# an object of a class is instantiated
# it allows initialisation - passing initial values to object


# class Pod:
#     def __init__(self, serial_number: str) -> None:
#         self.serial_number = serial_number

#     def power_on(self):
#         print("Powering on...")

#     def power_off(self):
#         print("Powering off...")

#     def hard_stop(self):
#         print("Initiating hard stop...")


# pod1 = Pod("INEVI0012445")

# pod1.power_on()
# print(pod1.serial_number)

# Class and Object Variables #

# Class variables are owned by the class
# Object variables are owned by the object / instance of that class


# class Server:
#     """
#     Server class
#     Creates instances of a server object
#     """

#     # class variable
#     quantity = 0

#     def __init__(self, serial_number: str) -> None:
#         self.serial_number = serial_number
#         print(f"The serial number is {serial_number}")
#         Server.quantity += 1

#     def power_on(self):
#         print(f"Powering on server {self.serial_number}")

#     @classmethod
#     def state_quantity(cls):
#         print("There are {:d} servers".format(cls.quantity))


# computer = Server("INEVI000234")
# computer1 = Server("INEVI00923")

# Server.state_quantity()
# print(Server.__doc__)

# Inheritance #

# A type / subtype relationship between classes


class Computer:
    def __init__(self, serial_number: str, size: str) -> None:
        self.serial_number = serial_number
        self.size = size

    def power_on(self):
        print("Powering on")

    def power_off(self):
        print("Powering off")

    def sleep(self):
        print("Hibernating...")


class Server(Computer):
    def __init__(self, serial_number: str, size: str, spec: dict[str, str]) -> None:
        super().__init__(
            serial_number, size
        )  # only pass the extra arguments expected by parent class, never `self`
        self.serial_number = serial_number
        self.size = size
        self.spec = spec


pod = Server(
    "INEVI1120234",
    "2U",
    {"GPU": "NVIDIA A1000 8G GPU", "CPU": "AMD THREADRIPPER PRO 9955WX"},
)
