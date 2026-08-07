# Decorators in Python

A **Decorator** is a function that takes another function as an argument, extends its behavior without explicitly modifying its source code, and returns a new function.

## Problems

Create a folder `08_decorators`.

### Problem 1: Timing Function Execution

Problem: Write a decorator that measures the time a function takes to execute.

Create a file `01_solution.py` inside `08_decorators` folder.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} seconds of time.")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)
```

Open Terminal and go to `08_decorators` directory.

```bash
$ python 01_solution.py 
example_function ran in 2.0005226135253906 seconds of time.
```

### Problem 2: Debugging Function Calls

Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

Create a file `02_solution.py` inside `08_decorators` folder.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", greeting="hanji")
```

Open Terminal and go to `08_decorators` directory.

```bash
$ python 02_solution.py 
calling: hello with args  and kwargs 
hello
calling: greet with args chai and kwargs greeting=hanji
hanji, chai
```

### Problem 3: Cache Return Values

Problem: Implement a decoratoor that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

Create a file `03_solution.py` inside `08_decorators` folder.

```python
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(4, 7))
print(long_running_function(2, 3))
```

Open Terminal and go to `08_decorators` directory.

```bash
$ python 03_solution.py 
{}
5
11
5
```