# Data Types in Python

## Comments

In VS Code, you can press `Ctrl + /` to comment a line or multiple lines.

Or you can type `#` and write a comment in a `.py` file.

## Object Types / Data Types

- Number: `1234`, `3.1415`, `3+4j`, `0b111`, `Decimal()`, `Fraction()`
- String: `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'`
- List: `[1, [2, 'three'], 4.5]`, `list(range(10))`; The values are indexed 0-based. You can also nest one list into another and keep values of any type. List also have some methods.
- Tuple: `(1, 'spam', 4, 'U')`, `tuple('spam')`, `namedtuple`
- Dictionary: `{'food': 'spam', 'taste': 'yum'}`, `dict(hours=10)`; We can have named indices.
- Set: `set('abc')`, `{'a', 'b', 'c'}`; only contains unique values
- File: `open('eggs.txt')`, `open(r'C:\ham.bin', 'wb')`
- Boolean: `True`, `False`; only one of two values is possible
- None: `None`; only one value is possible. `None` means nothing.
- Functions, modules, classes
- Advance: Decorators, Generators, Iterators, MetaProgramming

## Some Random Stuffs

Open Python shell.

### Calculations

```bash
>>> 12 + 12
24
```

Python supports high precision. If any number is a floating type, then the expression evaluates to a floating value.

```bash
>>> 2.5 * 5
12.5
```

You can calculate powers using `**`. Here, Python shines because Python can handle complex calculations easily.

```bash
>>> 2 ** 100
1267650600228229401496703205376
```

### Math module

```bash
>>> import math
```

Value of pi:

```bash
>>> math.pi
3.141592653589793
```

### Random module

```bash
>>> import random
```

Pick a random value from 0 to 1 (exclusive).

```bash
>>> random.random()
0.8335743089987432
```

Pick a random value from your choices.

```bash
>>> random.choice([1, 2, 3, 4, 5])
3
```

```bash
>>> random.choice([1, 2, 3, 4, 5])
5
```

### String

```bash
>>> username = "chaiaurcode"
```

You can find the length of a string using `len()`.

```bash
>>> len(username)
11
```

You can access a string character using 0-based indexing.

```bash
>>> username[0]
'c'
```

But if you try to change a character in a String, you will get an error. Because String is immutable.

```bash
>>> username[0] = 'A'
TypeError: 'str' object does not support item assignment
```

You can also use negative indexing in a String.

```bash
# This gives first character from end
>>> username[-1]
'e'
```

```bash
# This gives second character from end
>>> username[-2]
'd'
```

You can also extract a range of characters from a String. This is called **Slicing**.

```bash
# Extracts from index 1 to 2
>>> username[1:3]
'ha'
```

### `dir()` method

This built-in methods returns a sorted list of valid attributes and methods for any Python object.

```bash
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### List

```bash
>>> mylist = [123, "chai", 3.14]
```

```bash
>>> mylist
[123, 'chai', 3.14]
```

You can access an element by its 0-based index.

```bash
>>> mylist[0]
123
```

You can also use negative indexing.

```bash
# First element from last
>>> mylist[-1]
3.14
```

### Dictionary

```bash
>>> myD = {'one':'lemon', 'two':'ginger', 'comic':'naagraj'}
```

```bash
>>> myD
{'one': 'lemon', 'two': 'ginger', 'comic': 'naagraj'}
```

You can access an element only through the defined indices.

```bash
# Element with index 'comic'
>>> myD['comic']
'naagraj'
```

If you try to access an invalid index. You will get an error.

```bash
>>> myD['comics']
KeyError: 'comics'
```

### Tuple

```bash
>>> myTup = (1, 2, 4)
```

```bash
>>> myTup
(1, 2, 4)
```

You can access an element from 0-based indexing.

```bash
>>> myTup[0]
1
```

You can also find the length of a tuple.

```bash
>>> len(myTup)
3
```