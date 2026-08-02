# Behind the scene of Loops in Python

Python has reimagined loops.

There are **Iteration tools** like `for`, _comprehension_, etc.

Iteration can only happen on **iterable objects**. Examples are _lists_, _file_, etc.

## Python Interation Protocol Mechanism

The entire iteration engine operates on two hidden magic methods: `__iter__()` and `__next__()`.

### The 4-Step Lifecycle of a Loop

1. **The Handshake (`iter()`):** Python passes the target object to the built-in `iter()` function. This triggers the object's `__iter__()` method, which initializes and returns a completely separate **iterator object** tasked with tracking the positional state.

2. **The Request (`next()`):** The loop calls the built-in `next()` function on that new iterator. This invokes the `__next__()` method, telling the iterator to pass back the next available item in the sequence.

3. **The Execution:** If an item is fetched successfully, Python injects it into your loop variable and runs the indented code block beneath the loop.

4. **The Shutdown(`StopIteration`):** When there are no more items left, the `__next__()` method raises a built-in `StopIteration` exception. Instead of crashing your script, Python expects this signal, intercepts it, and cleanly breaks out of the loop.

## Some Random Stuffs

Create a folder `04_iteration_tools`. Inside this, create a file `chai.py`.

```python
import time
print("chai is here")
username = "hitesh"
print(username)
```

Open Terminal and go to `04_iteration_tools` folder. And enter `python` to open Python shell.

```bash
$ python
>>>
```

### Files in Python

```bash
# reference of a file
>>> f = open('chai.py')

# Read a line
>>> f.readline()
'import time\n'

# Read next line
>>> f.readline()
'print("chai is here")\n'

# Read next line
>>> f.readline()
'username = "hitesh"\n'

# Read next line
>>> f.readline()
'print(username)'

# returns '' everytime as the lines ended
>>> f.readline()
''
>>> f.readline()
''
```

Another method:

```bash
>>> f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "hitesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-13>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
```

### Loops in File

```bash
>>> f = open('chai.py')

# valid but less used now
# >>> for line in open('chai.py').readlines():

# preferred
>>> for line in open('chai.py'):
...     print(line)
... 
import time

print("chai is here")

username = "hitesh"

print(username)
```

Alternate method:

```bash
>>> f = open('chai.py')
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
...     
import time
print("chai is here")
username = "hitesh"
print(username)
```

### `not` keyword

```bash
>>> test = "hitesh"
>>> if not test:
...     print("chai")
...
# prints nothing

>>> test = ""
>>> if not test:
...     print("chai")
...
chai
```

### Play with lists

```bash
>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x00000323BE151410>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x00000323BE151410>
>>> I.__next__()
2
>>> I
<list_iterator object at 0x00000323BE151410>
>>> I.__next__()
3
>>> I
<list_iterator object at 0x00000323BE151410>
>>> I.__next__()
4
>>> I
<list_iterator object at 0x00000323BE151410>
>>> I.__next__()
Traceback (most recent call last):
  File "<python-input-28>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
```

> The `iter()` always stays at the starting position

### Files vs List

```bash
>>> f = open('chai.py')
>>> f
<_io.TextIOWrapper name='chai.py' mode='r' encoding='cp1252'>
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
```

```bash
>>> myNewList = [1, 2, 3]
>>> iter(myNewList) is myNewList
False
>>> iter(myNewList) is myNewList.__iter__()
False
```

### Dictionary

```bash
>>> D = {'a': 1, 'b': 2}
>>> for key in D.keys():
...     print(key)
...     
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x00000323BEE06F90>

# next() and __next__() are same
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<python-input-47>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
```

### Range

```bash
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<python-input-56>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
```