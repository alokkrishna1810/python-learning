# Lists in Python

Open Python shell

## Some Random Stuffs

### List introduction

```bash
>>> tea_varities = ["Black", "Green", "Oolong", "White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'White']
```

> You can also create a list using `list()` method.

### Accessing with index

List has 0-based indexing similar to Strings.

```bash
# returns first element
>>> print(tea_varities[0])
Black

# returns second element
>>> print(tea_varities[1])
Green
```

Negative indexing is also valid.

```bash
# return first element from last
>>> print(tea_varities[-1])
White
```

### Slicing

Slicing is also similar to String.

```bash
# return a list of elements from index 1 to 2
>>> print(tea_varities[1:3])
['Green', 'Oolong']

# return a list of elements from start to 1
>>> print(tea_varities[:2])
['Black', 'Green']

# return a list of elements from 2 to end
>>> print(tea_varities[2:])
['Oolong', 'White']
```

### Updating elements

```bash
# Update 4th element
>>> tea_varities[3] = "Herbal"
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Herbal']
```

### Updating a range of elements

```bash
# Replace elements from index 1 to 1
>>> tea_varities[1:2] = "Lemon" # treated as array
>>> tea_varities
['Black', 'L', 'e', 'm', 'n', 'o', 'n', 'Oolong', 'Herbal']
```

```bash
>>> tea_varities = ["Black", "Green", "Oolong", "White"]
# Try to replace with a list
>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
```

```bash
# Replace elements from index 1 to 2
tea_varities[1:3] = ["green", "Masala"]
>>> tea_varities
['Black', 'green', 'Masala', 'White']
```

```bash
# return empty array
>>> tea_varities[1:1]
[]

# inserts at index 1
>>> tea_varities[1:1] = ["test", "test"]
>>> tea_varities
['Black', 'test', 'test', 'green', 'Masala', 'White']
```

```bash
# deletes elements from index 1 to 2
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'green', 'Masala', 'White']
```

### Traversal in List

```bash
>>> for tea in tea_varities:
...     print(tea)
... 
Black
green
Masala
White
```

```bash
>>> for tea in tea_varities:
...     print(tea, end="-")
... 
Black-green-Masala-White-
```

### Conditionals in List

```bash
# check if "Oolong" is present
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
...
```

This gives no output as item was not found.

```bash
# inserts "Oolong" element at the end
>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'green', 'Masala', 'White', 'Oolong']

# check if "Oolong" is present
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
...
I have Oolong tea
```

### Removing elements in List

```bash
# returns last element and removes it
>>> tea_varities.pop()
'Oolong'
>>> tea_varities
['Black', 'green', 'Masala', 'White']
```

```bash
# removes a particular element
>>> tea_varities.remove("green")
>>> tea_varities
['Black', 'Masala', 'White']
```

### Inserting elements in List

```bash
# inserts at particular index
>>> tea_varities.insert(1, "green")
>>> tea_varities
['Black', 'green', 'Masala', 'White']
```

### Copy of list

```bash
# creates a shallow copy
>>> tea_varities_copy = tea_varities.copy()
```

```bash
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy.append("Lemon")

# original did not change
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White', 'Lemon']
```

### `range` method

```bash
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
```

### List comprehension

```bash
# creates a list of squares of numbers from 0 to 9
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```bash
# creates a list of cubes of numbers from 0 to 4
>>> cube_num = [x**3 for x in range(5)]
>>> squared_num
[0, 1, 8, 27, 64]
```