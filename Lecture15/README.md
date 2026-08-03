# Functions in Python

For functions, there are two things: Definition and Use.

## Problems

Create a folder `05_functions`.

### Problem 1: Basic Function Syntax

Problem: Write a function to calculate and return the square of a number

Create a file `01_solution.py` inside `05_functions` folder.

```python
# def square_of_num(number):
#     print(number ** 2)

# square_of_num(4)

# result = square_of_num(4) # does the work and returns None
# print(result) # prints None

def square_of_num(number):
    return number ** 2

result = square_of_num(4)
print(result)
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 01_solution.py
16
```

### Problem 2: Function with Multiple Parameters

Problem: Create a function that takes two numbers as parameters and returns their sum.

Create a file `02_solution.py` inside `05_functions` folder.

```python
def add(numOne, numTwo):
    return numOne + numTwo

print(add(5, 5))
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 02_solution.py
10
```

### Problem 3: Polymorphism in Functions

Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

> Python already follows polymorphism

```bash
>>> 5 * 5
25
>>> "h" * 5
'hhhhh'
```

Create a file `03_solution.py` inside `05_functions` folder.

```python
def multiply(p1, p2):
    return p1 * p2

print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(5, 'a'))
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 03_solution.py
40
aaaaa
aaaaa
```

### Problem 4: Function Returning Multiple Values

Problem: Create a function that returns both the area and circumference of a circle given its radius.

Create a file `04_solution.py` inside `05_functions` folder.

```python
import math

def circle_stats(radius):
    area =  math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference
    # print("hi") # code not reachable after return in function

a, c = circle_stats(3)

print("Area:", a, "Circumference:", c)
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 04_solution.py 
Area: 28.274333882308138 Circumference: 18.84955592153876
```

### Problem 5: Default Parameter Value

Problem: Write a function that greets a user. If no name is provided, it sould greet with a default name.

Create a file `05_solution.py` inside `05_functions` folder.

```python
def greet(name = "User"):
    return "Hello, " + name + "!"

print(greet())
print(greet("chai"))
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 05_solution.py 
Hello, User!
Hello, chai!
```

### Problem 6: Lambda Function

Problem: Create a lambda function to compute the cube of a number.

Create a file `06_solution.py` inside `05_functions` folder.

```python
cube = lambda x: x ** 3

print(cube(3))
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 06_solution.py 
27
```

### Problem 7: Function with *args

Problem: Write a function that takes variable number of arguments and returns their sum.

Create a file `07_solution.py` inside `05_functions` folder.

```python
def sum_all(*args): # can rename anything but args is conventional
    # print(*args) # prints all arguments
    # print(args) # prints a tuple containing all arguments
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 07_solution.py 
3
15
36
```

### Problem 8: Function with **kwargs

Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

Create a file `08_solution.py` inside `05_functions` folder.

```python
# def print_kwargs(name, power):
#     print("Name:", name, ", Power:", power)

# print_kwargs(name="Shaktiman", power="laser")
# print_kwargs(power="laser", name="Shaktiman") # You can change order for named arguments

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr.Jackaal")
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 08_solution.py 
name: shaktiman
power: lazer
name: shaktiman
name: shaktiman
power: lazer
enemy: Dr.Jackaal
```

### Problem 9: Generator Function with yield

Problem: Write a generator function that yields even numbers up to a specified limit.

Create a file `09_solution.py` inside `05_functions` folder.

```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 09_solution.py 
2
4
6
8
10
```

### Problem 10: Recursive Function

Problem: Create a recursive function to calculate the factorial of a number.

Create a file `10_solution.py` inside `05_functions` folder.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

Open Terminal and go to `05_functions` folder inside it.

```bash
$ python 10_solution.py 
120
```