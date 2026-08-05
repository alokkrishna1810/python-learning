# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car) # <__main__.Car object at 0x000002CB39A346E0>

class Car:
    total_car = 0 # class variable, means not for any individual object

    # constructor
    def __init__(self, brand, model):
        self.__brand = brand # becomes private to class, means cannot be accessed  outside the class, not even in the child
        self.__model = model
        Car.total_car += 1 # updates each time this constructor is called

    # getter
    def get_brand(self):
        return self.__brand + " !"

    # self gives the context of the current object
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod # a decorator that makes a function a class method
    def general_description(): # does not requires self parameter
        return "Cars are means of transport."

    @property # a deorator that makes a method like a variable call
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # super provides the context of parent class
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

# my_car = Car("Toyota", "Corolla")
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.full_name())

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.full_name)
# print(my_tesla.full_name())
# print(my_tesla.battery_size)

# print(my_tesla.get_brand())
# print(my_tesla.__brand) # AttributeError: 'ElectricCar' object has no attribute '__brand'.

# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())
# Car("Tata", "Nexon")

# print(safari.total_car)

# test = Car("test", "test")
# print(test.total_car)

# print(Car.total_car) # correct way to access class variable

# my_car = Car("Tata", "Safari")
# print(my_car.general_description())
# print(Car.general_description()) # correct way to call class method

# my_car.model = "City" # read-only, cannot be modified
# print(my_car.model)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())