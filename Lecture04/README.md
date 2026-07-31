# Immutable and Mutable in Python

```
          Data Types
              / \
             /   \
            /     \
           /       \
          /         \
    Mutable         Immutable
  Data Types       Data Types
      |                 |
      |                 |
      |                 |
-> List             -> Integers
-> Set              -> Floating-point numbers
-> Dictionary       -> Boolean
-> Bytearray        -> Strings
-> Array            -> Tuples
                    -> Frozen set
                    -> Bytes
```

> In Python, everything is created as an Object.

## Real Meaning of Mutable and Immutable

Open Python shell.

### Example 1

```bash
>>> username = "hitesh"
```

```bash
>>> username
'hitesh'
```

Now, change the value of `username`.

```bash
>>> username = "chaiaurcode"
```

```bash
>>> username
'chaiaurcode'
```

Here, the value of `username` changed. But `String` was immutable. **Why**?

In this scenario, only the reference changed, the String `"hitesh"` did not change. In the memory, a new String `"chaiaurcode"` created as another object and the reference of `username` changed from `"hitesh"` to `"username"`.

Once the **Garbage Collector** ensures there is no reference to the String Object `"hitesh"`, it is removed from the memory.

```
                    ref removed
    username ----------X---------> "hitesh" => no reference,
        \                                    so GC removed it
         \                                    from the memory.
          \
           \
            +-------------------> "chaiaurcode"
                new ref added
```

### Example 2

```bash
>>> x = 10
```

```bash
>>> y = x
```

```bash
>>> x
10
```

```bash
>>> y
10
```

Now, change the value of `x`.

```bash
>>> x = 15
```

```bash
>>> y
10
```

Here, we defined `y = x`. But when we changed the value of `x`, `y` did not change. Why?

In this scenario, `x = 10` means `x` points to `10`. After that, `y = x` means that the reference is copied to `y`. So `y` also points to `10`.

Now, `x = 15` means that the reference in `x` now points to `15`. But the reference in `y` did not change. So, `y` has the reference pointing to `10` and `x` pointing to `15`.

```
            new ref added
    x  ----------------------> 15
     \
      \
       \
        \    ref removed
         +----X------------------> 10
                              /
                             /
       +--------------------+
      /     ref did not change
     /
    y
```

**Mutable** objects allow you to change their content in-place without altering their memory location.

**Immutable** object cannot be modified; any operation that appears to alter them actually spawns a brand-new object in memory with a different unique identity.