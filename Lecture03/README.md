# Python in Shell

## Launch the IDLE

There is **IDLE (Integrated Development and Learning Environment)** that comes bundled automatically with most standard Python installations on Windows and MacOS. This is Python's built-in GUI text editor and shell.

You can open IDLE:

- directly from OS applications (Just search it and open it.)
- or from Terminal:

```bash
# For Windows
python -m idlelib

# For Mac/Linux
idle3
```

IDLE has the **shell window** that behaves exactly like the terminal shell but includes syntax highlighting and code auto-completion. Even you can also create files and run Python scripts inside the **editor window**.

## Launch the Interactive Shell (REPL)

The interactive shell (**Read-Eval-Print Loop**) lets you test code instantly, line by line.

### Start

1. Open your terminal.
2. Type the launch command and press Enter:

```bash
# Windows
python

# Windows
py

# macOS / Linux
python3
```

3. Look for the **prompt indicator** (`>>>`), which means Python is ready.

### Exit

For Windows, press `Ctrl + Z`, then press `Enter`. Or, `Ctrl + C` followed by `Ctrl + D` also works in some setup.

For macOS / Linux, press `Ctrl + D`.

Or, you can type either of these function calls directly into the `>>>` prompt and press `Enter`:
- `exit()`
- `quit()`

## Some Random Stuffs

Go to `01_basics` directory in the terminal inside VS Code. And open REPL.

### print something

```bash
>>> print("chai")
chai
```

### Calculations

```bash
>>> 2*2
4
```

```bash
>>> 3+5
8
```

### Testing

Testing is the real purpose of using REPL.

```bash
>>> "chai" * 4
'chaichaichaichai'
```

### Variables

Declaration and Initialization:

```bash
>>> score = 100
```

This will not give you any output. But when you write the variable name and press Enter, it gives you the value.

```bash
>>> score
100
```

If you try to get the value of any undeclared or uninitialized variable, it will throw error.

```bash
>>> tea
NameError: name 'tea' is not defined
```

### Modules

A **module** is simply a file containing Python code (with a `.py` extension) that you can reuse in other programs.

There are some built-in modules in Python.

You can import a module using `import`.

```bash
>>> import os
```

This does not give you any output. Now you can use the code defined in `os` module.

```bash
# Gets the current working directory
>>> os.getcwd()
'C:\\Users\\Alok Krishna\\Desktop\\python-learning\\Lecture01\\01_basics'
```

### Loops

In loops, you have to take care of indentation.

After putting a colon (`:`) at the end of `for` line, you will get `...` at each line after you write something on the particular line. When you keep a line empty, and press `Enter`, your code will be executed.

Each line in a loop should be written after 4 spaces.

```bash
# Prints each character of "chai" separated lines
>>> for c in "chai":
...     print(c)
...
c
h
a
i
```

### Import another module

```bash
import sys
```

```bash
# Gets the system platform
>>> sys.platform
'win32'
```

### Import custom modules

Ensure you are inside `01_basics` folder in the terminal. You already have a Python code file `hello_chai.py`.

```bash
import hello_chai
chai aur python
lemon tea
```

This gives an ouptut because there were executable lines written in it.

You can access methods by `module_name.method_name()`.

```bash
>>> hello_chai.chai("mint tea")
mint tea
```

Now update your code in `hello_chai.py`.

```python
print("chai aur python")

def chai(n):
    print(n)

chai("lemon tea")

chai_one = "lemon tea"
chai_two = "ginger tea"
chai_three = "masala chai"
```

If you try to access these new variables, you will get an error.

```bash
>>> hello_chai.chai_one
AttributeError: module 'hello_chai' has no attribute 'chai_one'
```

> **Note:** If you change anything in your module, the change will not be reflected automatically inside the REPL. To force the REPL to load your updated code without restarting the session, you must use the `importlib` module. Otherwise, if possible, close the REPL, and do all the things again. If you import the module again in the current session, Python completely skips re-reading the file to save time.

```bash
# imports a method from module
>>> from importlib import reload
```

Now reload the module.

```bash
>>> reload(hello_chai)
chai aur python
lemon tea
<module 'hello_chai' from 'C:\\Users\\Alok Krishna\\Desktop\\python-learning\\Lecture01\\01_basics\\hello_chai.py'>
```

Now, your module is updated in your REPL.

```bash
>>> hello_chai.chai_one
'lemon tea'
```

```bash
>>> hello_chai.chai_three
masala chai
```