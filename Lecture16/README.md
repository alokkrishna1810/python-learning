# Scopes and Closures in Python

A **scope** determines the exact region of a program where a specific variable is visible and accessible.

A **namespace** is the physical container (implemented as a dictionary) that stores variable names mapped to their objects.

**Variable Resolution:** When you reference a variable, Python searches for the name sequentially from the inside out using the **LEGB Rule**. It stops searching at the first match.

$$ \text{Local (L)} \to \text{Enclosing} \to \text{Global} \to \text{Built-in} $$

```
    +------------------------------------------------------------+
    |                                                            |
    | Built-in (e.g., print, len)                                |
    |   +---------------------------------------------------+    |
    |   | Global (Module-level)                             |    |
    |   |   +------------------------------------------+    |    |
    |   |   | Enclosing (Nested)                       |    |    |
    |   |   |   +------------------------------+       |    |    |
    |   |   |   | Local (Function)             |       |    |    |
    |   |   |   +------------------------------+       |    |    |
    |   |   +------------------------------------------+    |    |
    |   +---------------------------------------------------+    |
    +------------------------------------------------------------+
```

## Some Random Stuffs

Create a folder `06_scopes`. Inside it, create a file `01_scope.py`.

```python
username = "chaiaurcode"

def func():
    username = "chai"
    print(username) # prints "chai"

print(username) # prints "chaiaurcode"
func()
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py
chaiaurcode
chai
```

In this case, the `username` inside the function is a **local variable**. The `print()` function inside `func()` found a local variable and thus it printed `chai`. The **local variable** is valid inside the scope it is declared. So, the `print()` function outside `func()` does not recognize the local variable, but recognizes the **global variable** `username` that was declared globally outside the function `func()`. So, this prints `chaiaurcode`.

Now, update `01_scope.py` file.

```python
username = "chaiaurcode"

def func():
    # username = "chai"
    print(username) # prints "chaiaurcode"

print(username) # prints "chaiaurcode"
func()
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py 
chaiaurcode
chaiaurcode
```

Take another example. Update the content of `01_scope.py`.

```python
x = 99

def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py 
100
```

In this case, when the function `func2()` is called, it recognizes `y` parameter from the argument provided as `1`. It does not find `x` in its local scope but finds `x` in the global scope. So, it recognizes as `99`. Hence, the function returns `z` as `100`.

Take another example. Update the content of `01_scope.py`.

```python
x = 99

def func3():
    global x
    x = 12

func3()
print(x)
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py 
12
```

In this example, the statement `global x` states that the variable `x` inside `func3()` is not any other local scope variable, but it's from the global scope.

Take another example. Update the content of `01_scope.py`.

```python
x = 99

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py 
88
```

According to LEGB rule, the function prints `88`. If you comment `x = 88` line. Then, it will go one layer above and print `99`.

## Closures

A **closure** is a nested function object that retains access to variables from its enclosing scope, even after the outer function has finished executing.

Update the content of `01_scope.py`.

```python
x = 99

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py 
88
```

Take another example. Update the content of `01_scope.py`.

```python
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f)
print(g)
print(f(3))
print(g(3))
```

Open Terminal and go to `06_scopes` directory.

```bash
$ python 01_scope.py 
<function chaicoder.<locals>.actual at 0x0000028A7176F950>
<function chaicoder.<locals>.actual at 0x0000028A7176FA00>
9
27
```