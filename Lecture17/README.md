# Object-Oriented Programming in Python

## Problems

Create a folder `07_oop`.

### Problem 1: Basic Class and Object

Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

Inside `07_oop` folder, create a file `01_solution.py`.

```python
class Car:
    # constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Toyota
Corolla
Tata
Safari
```

### Problem 2: Class method and Self

Problem: Add a method to the Car class that displays the full name of the car (brand and model).

Update the `01.solution.py` file.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # self gives the context of the current object
    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.full_name())
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Toyota Corolla
Tata Safari
```

### Problem 3: Inheritance

Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

Update the `01.solution.py` file.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # super provides the context of parent class
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name)
print(my_tesla.full_name())
print(my_tesla.battery_size)
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Tesla
Model S
<bound method Car.full_name of <__main__.ElectricCar object at 0x000001B272EA46E0>>
Tesla Model S
85kWh
```

### Problem 4: Encapsulation

Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

Update the `01.solution.py` file.

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand # becomes private to class, means cannot be accessed  outside the class, not even in the child class
        self.model = model

    # getter
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.get_brand())
# print(my_tesla.__brand) # AttributeError: 'ElectricCar' object has no attribute '__brand'.
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Tesla !
```

### Problem 5: Polymorphism

Problem: Demonstrate polymorphism by defining a method feul_type in both Car and ElectricCar classes, but with different behviors.

Update the `01.solution.py` file.

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Electric charge
Petrol or Diesel
```

### Problem 6: Class Variables

Problem: Add a class variable to Car that keeps track of the number of cars created.

Update the `01.solution.py` file.

```python
class Car:
    total_car = 0 # class variable, means not for any individual object

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1 # updates each time this constructor is called

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # super provides the context of parent class
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
safari = Car("Tata", "Safari")
Car("Tata", "Nexon")

print(safari.total_car)
print(Car.total_car) # correct way to access class variable
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
3
3
```

### Problem 7: Static Method

Problem: Add a static method to the Car class that returns a general description of a Car.

Update the `01.solution.py` file.

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod # a decorator that makes a function a class method
    def general_description(): # does not requires self parameter
        return "Cars are means of transport."

my_car = Car("Tata", "Safari")
print(my_car.general_description())
print(Car.general_description()) # correct way to call class method
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Cars are means of transport.
Cars are means of transport.
```

### Problem 8: Property Decorators

Problem: Use a property decorator in the Car class to make the model attribute read-only.

Update the `01.solution.py` file.

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport."

    @property # a deorator that makes a method like a variable call
    def model(self):
        return self.__model

my_car = Car("Tata", "Safari")
# my_car.model = "City" # read-only, cannot be modified
print(my_car.model)
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
Safari
```

### Problem 9: Class Inheritance and isinstance() Function

Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

Update the `01.solution.py` file.

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport."

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
True
True
```

### Problem 10: Multiple Inheritance

Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

Update the `01.solution.py` file.

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport."

    @property
    def model(self):
        return self.__model

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
```

Open terminal and go to `07_oop` folder.

```bash
$ python 01_solution.py 
This is engine
this is battery
```