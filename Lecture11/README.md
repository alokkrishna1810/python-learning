# Tuples in Python

Lists are mutable. Tuples are immutable.

## Some Random Stuffs

### Tuples Introduction

```bash
>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
```

### Accessing elements

```bash
# 0-based indexing
>>> tea_types[0]
'Black'

# Negative indexing
>>> tea_types[-1]
'Oolong'
```

### Slicing

```bash
>>> tea_types[1:]
('Green', 'Oolong')
```

### Updating elements

Updating elements is not allowed in tuples as they are immutable.

```bash
>>> tea_types[0] = "Lemon"
TypeError: 'tuple' object does not support item assignment
```

### Length of tuple

```bash
>>> len(tea_types)
3
```

### Concatenation

```bash
>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Green', 'Oolong')
```

### Conditionals in Tuples

```bash
# Check presence of element
>>> if "Green" in all_tea:
...     print("I have green tea")
... 
I have green tea
```

### Counting elements in Tuples

```bash
>>> more_tea = ("Herbal", "Earl Grey", "Herbal")
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Herb")
0
```

### Unwrapping Tuples from Tuples

```bash
# number of elements on both sides must be same
>>> (black, green, Oolong) = tea_types
>>> black
'Black'
```

### `type()` method

```bash
>>> type(tea_types)
<class 'tuple'>
```

### Nested Tuples

```bash
>>> ("", (1, 2, 3), "")
('', (1, 2, 3), '')
```