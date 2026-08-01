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