# Strings in Python

Python was purposely designed for Scientific community.

## Some Random Stuffs

Open Python shell.

In Python, Strings are avaialable in single quotes (`' '`), double quotes (`" "`), triple single quotes (`''' '''`), or double quotes (`""" """`).

### String introduction

```bash
>>> chai = "Lemon Chai"
```

```bash
>>> chai
'Lemon Chai'
```

The above way is valid for shell only. For code, you can use `print()` method.

```bash
>>> print(chai)
Lemon Chai
```

### Updating values

```bash
>>> chai = "Masala Chai"
```

### Accessing elements

```bash
>>> first_char = chai[0]
```

```bash
>>> print(first_char)
M
```

### Slicing

```bash
>>> chai
'Masala Chai'
```

```bash
# extracts elements 0 to 5
>>> slice_chai = chai[0:6]
```

```bash
>>> print(slice_chai)
Masala
```

```bash
>>> num_list = "0123456789"
```

```bash
>>> num_list[:]
'0123456789'
```

```bash
>>> num_list[3:]
'3456789'
```

```bash
>>> num_list[:7]
'0123456'
```

```bash
# hops (offset)
>>> num_list[0:7:2]
'0246'
```

```bash
# hops (offset)
>>> num_list[0:7:3]
'036'
```

### Negative indexing

```bash
# 1st element from last
>>> chai[-1]
'i'
```

### String Methods or Functions

```bash
>>> chai
'Masala Chai'
```

```bash
# Converts all characters to lower case
>>> print(chai.lower())
masala chai
```

```bash
# Converts all characters to upper case
>>> print(chai.upper())
MASALA CHAI
```

```bash
>>> chai = "   Masala Chai   "
>>> chai
'   Masala Chai   '

# Truncate all the whitespaces before and after the string
>>> print(chai.strip())
Masala Chai
```

```bash
>>> chai = "Lemon Chai"

# Find "Lemon" and replace with "Ginger"
>>> print(chai.replace("Lemon", "Ginger"))
Ginger Chai
```

```bash
>>> chai = "Lemon, Ginger, Masala, Mint"

# Splits strings by spaces and converts to list of strings
>>> print(chai.split())
['Lemon,', 'Ginger,', 'Masala,', 'Mint']

# Splits strings by given string and converts to list of strings
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
```

```bash
>>> chai = "Masala Chai"

# Finds a string and returns the index of first character
>>> print(chai.find("Chai"))
7

# If item is not found, return -1
>>> print(chai.find("chai"))
-1
```

```bash
>>> chai = "Masala Chai Chai Chai Chai"

# return count of an item
>>> print(chai.count("Chai"))
4
```

### Placeholders

```bash
>>> chai_type = "Masala"
>>> quantity = 2

# placeholders for variables
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'

# placing variables in placeholders
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai
```

### List to String

```bash
>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']

# joins all the strings together to make a string
>>> print("".join(chai_variety))
LemonMasalaGinger

# join all strings by spaces
>>> print(" ".join(chai_variety))
Lemon Masala Ginger

# join all strings by dashes
>>> print("-".join(chai_variety))
Lemon-Masala-Ginger

# join all strings by comma followed by space
>>> print(", ".join(chai_variety))
Lemon, Masala, Ginger
```

### Length of a String

```bash
>>> chai = "Masala Chai"

# returns the length of the string
>>> print(len(chai))
11
```

### Traversal in String

```bash
# prints all the characters in separate lines
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a

C
h
a
i
```

### Special characters inside String

For quotes, you can put a double quote inside a single quote or vice versa.

```bash
# A backward slash (\) allows one single special character just after it
>>> chai = "He said, \"Masala chai is awesome\" "
>>> chai
'He said, "Masala chai is awesome"'
```

```bash
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai

# Use r before quotes of String to consider everything as raw string
>>> chai = r"Masala\nchai"
>>> print(chai)
Masala\nchai
```

```bash
# Don't put a backward slash at the end
>>> chai = r"c:\user\pwd\"
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
```
```bash
>>> chai = r"c:\\user\\pwd\\"
>>> print(chai)
c:\\user\\pwd\\
```

```bash
>>> chai = r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
```

```bash
# without r, you may get error in these cases
>>> chai = "c:\user\pwd"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
```

```bash
# You can also use backward (\) before another to cancel their effect
>>> chai = "c:\\user\\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
```

### Check presence of literals

```bash
>>> chai = "Masala Chai"

# in keyword
>>> print("Masala" in chai)
True
>>> print("Masalaa" in chai)
False
```