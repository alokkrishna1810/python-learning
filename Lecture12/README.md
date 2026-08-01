# Conditionals in Python

Python is a very straight-forward language.

## Problems

Create a folder `02_conditionals`.

### Problem 1: Age Group Categorization

Problem: Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

```bash
# Taking an input
>>> userscore = input("Give me a score value: ")
Give me a score value: 200
>>> userscore
'200'
>>> usercore / 2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> userscore_in_int = int(userscore)
>>> userscore_in_int
200
```

Create a file `01_solution.py` inside `02_conditionals`.

```python
# age = int(input("Provide me an age: "))

# Or

# age = input("Provide me an age: ")
# age_in_int = int(age)

age = 25

# A colon (:) starts a block and the indentation (tab) represents a block

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 01_solution.py 
Adult

```

### Problem 2: Movie Ticket Pricing

Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

Create a file `02_solution.py` inside `02_conditionals`.

```python
age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $", price)
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 02_solution.py 
Ticket price for you is $ 10

```

### Problem 3: Grade Calculator

Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

Create a file `03_solution.py` inside `02_conditionals`.

```python
score = 85

if score > 100:
    print("Please verify your score again")
    exit() # ends the program

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 03_solution.py 
Grade: B

```

### Problem 4: Fruit Ripeness Checker

Problem: Determine if a fruit is ripe,, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

Create a file `04_solution.py` inside `02_conditionals`.

```python
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 04_solution.py 
Ripe

```

### Problem 5: Weather Activity Suggestion

Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

Create a file `05_solution.py` inside `02_conditionals`.

```python
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 05_solution.py 
Go for a walk

```

### Problem 6: Transportation Mode Selection

Problem: Choose a mode of transportation based on the distance (e.g., < 3km: Walk, 3-15km: Bike, >15km: Car)

Create a file `06_solution.py` inside `02_conditionals`.

```python
distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of", transport)
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 06_solution.py 
AI recommends you the transport of Bike

```

### Problem 7: Coffee Customization

Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

Create a file `07_solution.py` inside `02_conditionals`.

```python
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order:", coffee)
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 07_solution.py 
Order: Medium coffee with an extra shot

```

### Problem 8: Password Strength Checker

Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), > 10 chars (Strong).

Create a file `08_solution.py` inside `02_conditionals`.

```python
password = "Secure3P@ss"
password_length = len(password)

if password_length < 6:
    strength = "Weak"
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is:", strength)
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 08_solution.py 
Password strength is: Strong

```

### Problem 9: Leap Year Checker

Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

Create a file `09_solution.py` inside `02_conditionals`.

```python
year = 2026

if (year % 400 == 0) or (year % 4 == 0 and year % 100):
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 09_solution.py 
2026 is NOT a leap year

```

### Problem 10: Pet Food Recommendation

Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: < 2 years - Puppy food, Cat: > 5 years - Senior cat food).

Create a file `10_solution.py` inside `02_conditionals`.

```python
animal = "Cat"
age = 7

if animal == "Dog" and age < 2:
    print("AI recommends Puppy Food.")
elif animal == "Cat" and age > 5:
    print("AI recommends Senior cat food.")
else:
    print("Sorry! The recommended food provided animal or age is not available.")
```

Open Terminal and go to `02_conditionals` folder inside it.

```bash
python 10_solution.py 
AI recommends Senior cat food.

```