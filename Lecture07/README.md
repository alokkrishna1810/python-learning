# Numbers in Python

Python has large circle of numbers as compared to other languages. By adding few libraries like Numpy, the paradigm of numbers are open widely. You can do almost all things that is done in MATLAB which may have some licensing issues.

Numbers are in fact group of data types. They include integers, floating numbers, fractions, decimals, complex, etc. In facts, Sets and Booleans are much similar treated as Numbers.

## Random Stuffs

Open Python shell.

### Operations

```bash
>>> x = 2
```

```bash
>>> y = 3
```

```bash
>>> z = 4
```

You can do basic arithmetic operations on numbers like add (`+`), subtract (`-`), multiply (`*`), power (`**`), divide (`/` or `//`) and remainder (`%`).

```bash
>>> x+y
5
```

You should take care of **operator precedence**. But it's always a good practice to use parenthesis (`( )`) to make the expression readable. Also, parenthesis (`( )`) have the highest preference.

```bash
>>> (x + y) * z
20
```

You can also do operations between an integer and a floating-point number. Python always prefers high precision.

```bash
>>> 40 + 2.23
42.23
```

But it is always recommended that you ensure the operation is between same data types explicitly. Otherwise, you may get undesired results or errors.

```bash
>>> 'hitesh' + 3
TypeError: can only concatenate str (not "int") to str
```

You can explicitly convert data types of Numbers.

```bash
>>> int(2.23)
2
```

```bash
>>> float(40)
40.0
```

**Operator Overloading** is present in Python too.

```bash
>>> 'chai' + 'code'
'chaicode'
```

You can also show multiple values separated with commas. They will form a tuple.

```bash
>>> x, y, z
(2, 3, 4)
```

In fact, you can also print results of multiple expressions, separated with commas.

```bash
>>> x + 1, y * 2
(3, 6)
```

Python can also handle very large numbers easily.

```bash
>>> 2 ** 100
1267650600228229401496703205376
```

```bash
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

### `repr()`, `str()`, and `print()`

```bash
>>> repr('chai')
"'chai'"
```

```bash
>>> str('chai')
'chai'
```

```bash
>>> print('chai')
chai
```

### Comparision

You have comparision operators like `>`, `<`, `>=`, `>=`, `==`, `!=`. They always return `True` or `False`. In fact, in Python, `True` and `False` are just special representations of `1` and `0`. Mathematically, they are same under the hood.

```bash
>>> 1 < 2
True
```

```bash
>>> 5.0 == 5.0
True
```

```bash
>>> 4.0 != 5.0
True
```

You can also use these types of comparisions:

```bash
>>> x < y < z
True
```

This is a shorthand for:

```bash
# and returns True only if both expressions are True
>>> x < y and y < z
True
```

One more example:

```bash
>>> 1 == 2 < 3
False
```

This is same as:

```bash
>>> 1 == 2 and 2 < 3
False
```

These shorthands are valid but not preferred because they are not readable.

### `math` module

```bash
>>> import math
```

Floor (closest small integer):

```bash
>>> math.floor(3.5)
3
```

```bash
>>> math.floor(-3.5)
-4
```

```bash
>>> math.floor(3.9)
3
```

Truncate (integer closest towards 0):

```bash
>>> math.trunc(2.8)
2
```

```bash
>>> math.trunc(-2.8)
-2
```

### Precision

You can handle large numbers with high precision in python easily.

```bash
>>> 999999999999999999999999999 + 1
1000000000000000000000000000
```

```bash
>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376
```

But for floating-point numbers, sometimes precision is lost.

```bash
>>> 999999999999999999999999999 * 2.1
2.1000000000000002e+27
```

### Imaginary or Complex Numbers

```bash
>>> 2 + 1j
(2+1j)
```

```bash
>>> (2 + 1j) * 3
(6+3j)
```

### Different nummber systems

```bash
# Octal: 0O or 0o
>>> 0o20
16
```

```bash
# Hexadecimal: 0X or 0x
>>> 0xFF
255
```

```bash
# Binary: 0B or 0b
>>> 0b1000
8
```

```bash
# integer to octal
>>> oct(64)
'0o100'
```

```bash
# integer to hexadecimal
>>> hex(64)
'0o40'
```

```bash
# integer to binary
>>> bin(64)
'0b1000000'
```

```bash
>>> int(64)
64
```

```bash
# octal to integer
>>> int('64', 8)
52
```

```bash
# hexadecimal to integer
>>> int('64', 16)
100
```

```bash
# binary to integer
>>> int('10000', 2)
16
```

### Bit manipulation

There are bit manipulation operators such as `|`, `&`, `^`, `~`, `<<`, `>>`.

Left shift (`<<`):

```bash
>>> x = 1
```

```bash
>>> x << 2
4
```

### `random` module

```bash
>>> import random
```

```bash
# random value from 0 to 1
>>> random.random()
0.016495322098005083
```

```bash
# random integer from 1 to 10
>>> random.randint(1, 10)
5
```

Random value from your choice list.

```bash
>>> l1 = ['lemon', 'masala', 'ginger', 'mint']
```

```bash
>>> random.choice(l1)
'masala'
```

Shuffle your list.

```bash
>>> random.shuffle(l1)
>>> l1
['masala', 'ginger', 'lemon', 'mint']
```

### Back to floating precision

```bash
>>> 0.1 + 0.1 + 0.4
0.6000000000000001
```

```bash
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
```

```bash
>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17
```

### `decimal` module

```bash
# imports Decimal class from decimal module
>>> from decimal import Decimal
```

```bash
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
```

```bash
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
```

### `fractions` module

```bash
# import Fraction class from fractions module
>>> from fractions import Fraction
```

```bash
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)
```

### Sets

```bash
>>> setone = {1, 2, 3, 4}
```

```bash
# intersection
>>> setone & {1, 3}
{1, 3}
```

```bash
# union
>>> setone | {1, 3, 7}
{1, 2, 3, 4, 7}
```

```bash
# difference
>>> setone - {1, 2, 3, 4}
set()
```

`set()` is not `{}`. Because `{}` is dictionary.

```bash
>>> type({})
<class 'dict'>
```

### Booleans

```bash
>>> type(True)
<class 'bool'>
```

`True` and `False` are special representations of `1` and `0`.

```bash
>>> True == 1
True
```

```bash
>>> False == 0
True
```

```bash
>>> True is 1
SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
```

```bash
>>> True + 4
5
```