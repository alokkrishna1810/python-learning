# Loops in Python

Loops are treated differently in Python.

An **iterable** is any Python object that you can loop over. `iter()` is the built-in function used to convert the iterable into an iterator.

## Problems

Create a folder `03_loops`.

### Problem 1: Counting Positive Nummber

Problem: Given a list of numbers, count how many are positive.

```bash
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
```

Inside `03_loops` folder, create a file `01_solution.py`.

```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of positive numbers is:", positive_number_count)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 01_solution.py
Final count of positive numbers is: 6

```

### Problem 2: Sum of Even Numbers

Problem: Calculate the sum of even numbers up to a given number n.

Inside `03_loops` folder, create a file `02_solution.py`.

```python
n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i

print("Sum of even numbers is:", sum_even)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 02_solution.py
Sum of even numbers is: 30

```

### Problem 3: Multiplication Table Printer

Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

Inside `03_loops` folder, create a file `03_solution.py`.

```python
number = 3

for i in range(1, 11):
    if i == 5:
        continue # skips remaining code of current iteration
    print(number, "x", i, "=", number * i)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 03_solution.py
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

```

### Problem 4: Reverse a String

Problem: Reverse a string using a loop

Inside `03_loops` folder, create a file `04_solution.py`.

```python
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 04_solution.py
nohtyP

```

### Problem 5: Find the First Non-Repeated Character

Problem: Given a string, find the first non-repeated character.

Inside `03_loops` folder, create a file `05_solution.py`.

```python
input_str = "teeter"

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is:", char)
        break # end the loop
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 05_solution.py
Char is: r

```

### Problem 6: Factorial Calculator

Problem: Compute the factorial of a number using a while loop.

Inside `03_loops` folder, create a file `06_solution.py`.

```python
# 5! = 5 * 4 * 3 * 2 * 1

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial:", factorial)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 06_solution.py
Factorial: 120

```

### Problem 7: Validate Input

Problem: Keep asking for user for input until they enter a number between 1 and 10.

Inside `03_loops` folder, create a file `07_solution.py`.

```python
while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again.")
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 07_solution.py
Enter a number between 1 and 10: 77
Invalid number, try again.
Enter a number between 1 and 10: 88
Invalid number, try again.
Enter a number between 1 and 10: 99
Invalid number, try again.
Enter a number between 1 and 10: 11
Invalid number, try again.
Enter a number between 1 and 10: 9
Thanks

```

### Problem 8: Prime Number Checker

Problem: Check if a number is prime.

Inside `03_loops` folder, create a file `08_solution.py`.

```python
number = 29
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 08_solution.py
True

```

### Problem 9: List Uniqueness Checker

Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

```bash
items = ["apple", "banana", "orange", "apple", "mango"]
```

Inside `03_loops` folder, create a file `09_solution.py`.

```python
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:", item)
        break
    unique_item.add(item)
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 09_solution.py
Duplicate: apple

```

### Problem 10: Exponential Backoff

Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

Inside `03_loops` folder, create a file `10_solution.py`.

```python
import time

wait_time = 1 # in seconds
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
```

Open the Terminal and go to `03_loops` directory inside it.

```bash
$ python 10_solution.py
Attempt 1 - wait time 1 seconds
Attempt 2 - wait time 2 seconds
Attempt 3 - wait time 4 seconds
Attempt 4 - wait time 8 seconds
Attempt 5 - wait time 16 seconds

```