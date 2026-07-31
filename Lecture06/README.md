# Internal Working of Python

## Reference Count

Every time you create an object in Python, the interpreter tracks how many aliases or variables points to it. When this nuber hits **zero**, the Garbage Collector immediately destroys the object and reclaims its memory.

### Checking reference counts

Open Python shell.

```bash
>>> import sys
```

Now, check the reference count of a random number, let's say `24601` or a string `'hitesh'`.

```bash
>>> sys.getrefcount(24601)
3221225472
```

```bash
>>> sys.getrefcount('hitesh')
3221225472
```

Even if you check for `'h'` or `1`, you will get the repeated results.

```bash
>>> sys.getrefcount('h')
3221225472
```
```bash
>>> sys.getrefcount(1)
3221225472
```

**This is happening because you cannot reliably determine the exact reference counts anymore, and the language is explicitly moving away from letting you do so.**

## Variables do not have data type in Python

In Python, a variable only have the reference to an Object. The Objects do have data types. But a variable don't have any data type in Python.

Open Python shell.

```bash
>>> a = 3
```

```bash
>>> a
3
```

Now, if you assign a value of different data type to `a`. There will be no error.

```bash
>>> a = 'chaiaurcode'
```

```bash
>>> a
'chaiaurcode'
```

In this scenario, the reference of `a` just changed from `3` to `'chaiaurcode'`.

```
        ref removed
    a -----X--------> 3
    \
     \
      \
       +------------> 'chaiaurcode'
       new ref added
```

> **Note:** Numbers and Strings are treated differently by the Garbage Collector. They are not instantly removed on zero reference counts. They are kept in the memory for some time.

## Some Random Stuffs

Open Python shell.

### Adding two numbers

```bash
>>> a = 5
```

```bash
>>> b = 2
```

```bash
>>> a
5
```

```bash
>>> b
2
```

Now add:

```bash
>>> a = a + 2
```

```bash
>>> a
7
```

```
    a -----------> 5

    b -----------> 2

    a = a + 2 = 5 + 2 = 7

        ref removed
    a -----X------> 5 (remains in memory for some time)
     \
      \
       \
        +--------> 7
        new ref added
```

### List

Lists are mutable.

```bash
>>> myListOne = [1, 2, 3]
```

```bash
>>> myListTwo = myListOne
5
```

```
    myListOne ------------> [1, 2, 3]
                        /
              +--------+
             /
            /
    myListTwo
```

Now, assign a String object to `myListOne`.

```bash
>>> myListOne = 'chai'
```

```bash
>>> myListTwo
[1, 2, 3]
```

In this scenario, the reference of `myListOne` changed but `myListTwo` did not change its reference.

```
         new ref added
          +---------> 'chai'
         /
        /       ref removed
    myListOne -----X-------> [1, 2, 3]
                        /
              +--------+
             /ref did not change
            /
    myListTwo
```

Now, we `myListOne` to the previous list.


```bash
>>> myListOne = [1, 2, 3]
```

Now, change any element of `myListOne`.


```bash
>>> myListOne[0] = 33
```

Check if `myListTwo` changed.


```bash
>>> myListTwo
[1, 2, 3]
```

Here, we assigned `[1, 2, 3]` to `myListOne`. This does refer to the same object as that of `myListTwo`. This created another object `[1, 2, 3]`.

```
    myListTwo ------------> [1, 2, 3]
                        
                ref removed
              +-----X------> 'chai'
             /
            /
    myListTwo --------------> [1, 2, 3] (new object created)
                new ref added
```

### Another list

```bash
>>> l1 = [1, 2, 3]
```

```bash
>>> l2 = l1
```

```bash
>>> l1
[1, 2, 3]
```

```bash
>>> l2
[1, 2, 3]
```

Now, change any element of `l1`.

```bash
>>> l1[0] = 44;
```

Now, if we check `l1` and `l2`. Both changed.

```bash
>>> l1
[44, 2, 3]
```

```bash
>>> l2
[44, 2, 3]
```

In this scenario, `l2 = l1` copied the reference of `l1` to `l2`. So, both refer to the same list object. So, if the object changes, the change will be visible to every pointing reference.

```
    l1 ------------> [1, 2, 3] => (change 1 to 42)
                        /
              +--------+
             /
            /
         l2

    Since list is mutable, no new object created, just the
    element changed.

    And since both l1 and l2 are pointing to the same object,
    the change is visible in both.

    l1 ------------> [44, 2, 3]
                        /
              +--------+
             /
            /
         l2
```

### One more list

```bash
>>> p1 = [1, 2, 3]
```

```bash
>>> p2 = p1
```

```bash
>>> p2 = [1, 2, 3]
```

Now, change any element of `p1`.

```bash
>>> p1[0] = 55
```

Check if both `p1` and `p2` changed.

```bash
>>> p1
[55, 2, 3]
```

```bash
>>> p2
[1, 2, 3]
```

In this scenario, the momeent we assigned `[1, 2, 3]` to `p2`, the reference of `p2` changed and it is now pointing to a new object. So, both `l1` and `l2` are pointing to different objects. Hence, change in one object does not affect another object.

```

    l1 --------------------> [1, 2, 3] => change 1 to 55
            ref removed  /
      +---------X-------+
     /
    l2---------------------> [1, 2, 3] (new object created)
        new ref added


    Before the change, since both l1 and l2 were pointing to different objects, the change in one does not affect other.

    l1 --------------------> [55, 2, 3]

    l2 ---------------------> [1, 2, 3]
```

### Slicing

```bash
>>> h1 = [1, 2, 3]
```

```bash
# Extracts all elements of h1 and put into h2
>>> h2 = h1[:]
```

```bash
>>> h2
[1, 2, 3]
```

If you change any element of `h1`, it will not reflect to `h2` as `h2` to pointing to a new object `[1, 2, 3]`.

```bash
>>> h1[0] = 55
```

```bash
>>> h1
[55, 2, 3]
```

```bash
>>> h2
[1, 2, 3]
```

```

    h1 ------------------------> [1, 2, 3] => change 1 to 55


    h2 = h1[:] ===> creates a new object [1, 2, 3]
     \
      \
       +-----------------------> [1, 2, 3]

    After the change,

    h1 -------------------> [55, 2, 3]

    h2 -------------------> [1, 2, 3]
```

### Deep copy vs Shallow Copy

A **shallow copy** constructs a new collection object but populates it with references to the child objects found in the original.

A **deep copy** recursively constructs a new collection object and duplicates all child objects, ensuring complete independence.

You can create shallow and deep copies using `copy` module.

```bash
>>> import copy
```

```bash
>>> h2 = copy.copy(h1)
```

```bash
>>> h2 = copy.deepcopy(h1)
```

| Feature | Reference Assignment (`b = a`) | Shallow Copy (`copy.copy()`) | Deep Copy (`copy.deepcopy()`) |
|---|---|---|---|
| **New Outer Container?** | No | Yes | Yes |
| **New Nested Objects?** | No | No (References shared) | Yes (Fully duplicated) |
| **Modifying Top-level Elements** | Affects both | Affects only the copy | Affects only the copy |
| **Modifying Nested Elements** | Affects both | Affects both | Affects only the copy |
| **Speed & Memory Efficiency** | Highest | Fast & Lightweight | Slower & uses more memory |

> A **slicing copy** creates a shallow copy (`h2 = h1[:]`). Slicing is heavily optimized in CPython. For flat lists, using `[:]` is often slightly faster than calling `copy.copy()` because it avoids the overhead of a Python function lookup.

### Equal variables and equal objects

In Python, the `==` operator checks for value equality, while the `is` operator checks for object identity.

```bash
>>> n = [1, 2, 3]
```

```bash
>>> m = n
```

```bash
>>> m
[1, 2, 3]
```

```bash
>>> n
[1, 2, 3]
```

Now, check for equality.

```bash
>>> m == n
True
```

```bash
>>> m is n
True
```

If you assign them separately with similar values, then it's different.

```bash
>>> n = [1, 2, 3]
```

```bash
>>> m = [1, 2, 3]
```

Check equality:

```bash
>>> m == n
True
```

```bash
>>> m is n
False
```

This happened because both point to different objects. But they have same values.