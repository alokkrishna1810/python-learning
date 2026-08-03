# def print_kwargs(name, power):
#     print("Name:", name, ", Power:", power)

# print_kwargs(name="Shaktiman", power="laser")
# print_kwargs(power="laser", name="Shaktiman") # You can change order for named arguments

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr.Jackaal")