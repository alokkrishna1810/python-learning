# Python Inner Working

When you execute a Python script / program (`.py` file), first you need a **Python interpreter**. This converts your script into **Byte code**. This byte code (`.pyc` file) is mostly hidden. In some cases, it becomes visible (e.g., when you import file).

When you install Python, there comes an inclusive **Python Virtual Machine**. This actually runs your code. Byte code is fetched into Python VM and run inside it.

## 1. Compile to Byte Code

This does not mean exact compilation. This is just a tech jargon.

**Byte Code** is a low-level code (but not machine code). It is platform-independent, means this can be executed on any machine if Python VM is installed on the machine.

### Byte Code runs faster

Byte code is generated after checking the syntax, parsing, etc. (not completely, but mostly). That is why, byte code runs faster than the script.

### Frozen Binaries

A **frozen binary** is a standalone, self-contained executable file (like an `.exe` on Windows or a binary script on Linux) that bundles your Python code, the Python runtime environment, and all dependencies into a single package.

Unlike a `.pyc` file, a frozen binary **does not require Python to be installed** on the target machine.

### `__pycache__` folder

This is a directory automatically created by Python to store **compiled bytecode (`.pyc` files)** of imported modules.

It acts as a performace cache so Python doesn't have to re-translate your human-readable source code into bytecode every time a script runs.

Inside this folder, you will see files named like `module_name.cpython-314.pyc` (e.g., we have seen `hello_chai.cpython-314.pyc`).

- `module_name`: The name of your original `.py` file.
- `cpython-314`: The Python implementation (CPython is usually the standard) and version (3.14) used to compile it, ensuring different Python versions don't conflict.

> **Note:** Python only creates `__pycache_` for files that are **imported** by other scripts, not usually for the main script you execute directly.

When you modify your `.py` file, Python checks the internal `__pycache__` file and compares its embedded timestamp / hash against your newly modified `.py` file.

## 2. Python Virtual Machine (PVM)

This is the runtime engine of Python. It is the software component that actually executes your program's instructions.

This is essentially a continuous loop at its lowest level. When your program runs, the PVM enters a massive, infinite loop that processes bytecode instructions one by one until the program ends or exits. This is why **Python is an interpreted language**.

> Python 3.13+ now includes an optional **Just-In-Time Compiler**. When the PVM loop identifies "hot code" (a piece of bytecode running repeatedly), it compiles that specific loop iteration directly into machine code, bypassing the interpreter loop entirely for those instructions.

### Bytecode is not machine code

A bytecode is an intermediate, low-level instruction set designed specifically for a **software-emulated** CPU (the PVM). It consists of generic, platform-independent operation codes (opcodes). It is completely cross-platform. A bytecode (`.pyc` file) generated on an Intel Windows PC will run perfectly on an ARM Mac or a Linux server, because bytecode does not care about physical hardware.

A machine code is the raw, native binary instructions (`0`s and `1`s) that a physical, hardware CPU (like Intel Core, AMD Ryzen, or Apple M-series chips) understands directly. It consists of architecture-specific instructions (assembly code). It is locked to a specific hardware architecture and OS. An executable binary compiled for Windows x86 will crash instantly if you try to run it natively on a Mac or Linux.

### Python Implementations

When you download Python from the official website, you are downloading **CPython**. In most cases, you will be using this only.

For other implemetations, you have to specifically mention them.

- `jython` (called j Python): compiles Python code into Java bytecode.
- `IronPython`
- `Stackless`: mainly used for concurrency
- `PyPy`: mainly for performance oriented