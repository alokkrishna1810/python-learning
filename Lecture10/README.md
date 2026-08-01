# Dictionary in Python

Order is important in List. The index of an element is a **key** to the element value.

In dictionary, order is not important. You assign manual keys to the elements. And, every element or item is a key-value pair.

## Some Random Stuffs

Open Python shell

### Dictionary Introduction

You can create a dictionary using `dict()` method or directly using key-value pairs separated by commas inside curly braces (`{ }`).

```bash
>>> chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
```

### Accessing elements

```bash
# using square braces ([])
>>> chai_types["Masala"]
'Spicy'

# an invalid key gives error
>>> chai_types["Masalaa"]
KeyError: 'Masalaa'
```

```bash
# using get() method
>>> chai_types.get("Ginger")
'Zesty'

# no output on invalid key
>>> chai_types.get("Gingery")
```

### Updating elements

```bash
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
```

### Loops in dictionary

```bash
# print the keys
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green
```

```bash
# print keys and values
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh
```

```bash
# alternate way
>>> for key, value in chai_types.items():
...     print(key, value)
... 
Masala Spicy
Ginger Zesty
Green Fresh
```

### Conditionals in Dictionary

```bash
# check if key is present
>>> if "Masala" in chai_types:
...     print("I have masala chai")
... 
I have masala chai
```

### Length of dictionary

```bash
# len() method
>>> print(len(chai_types))
3
```

### Inserting elements

```bash
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
```

### Removing elements

```bash
# pop() requires a key; returns the value and removes
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
```

```bash
# returns the last item with key-value as tuple and removes
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
```

```bash
# del is a universal keyword; it works for all objects and deletes from the memory
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
```

### copy a dictionary

```bash
# creates a shallow copy
>>> chai_types_copy = chai_types.copy()
```

### Nested Dictionary

Just like lists, you can nest dictionaries.

```bash
>>> tea_shop = {
... "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
... "Tea": {"Green": "Mild", "Black": "Strong"},
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black: Strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black: Strong'}}
```

```bash
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
```

### Dictionary Comprehension

```bash
>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```bash
# makes the dictionary empty
>>> sqaured_num.clear()
>>> sqaured_num
{}
```

### Creatings dictionary from key and value lists

```bash
>>> keys = ["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
```

```bash
>>> new_dict = dict.fromkeys(keys, keys)
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
```