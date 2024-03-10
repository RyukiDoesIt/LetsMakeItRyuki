# Trying the code
try:
    # Taking input
    x = int(input("What's x? "))
except ValueError:
    # If ValueError is True
    print("x is not an integer!")

# Printing output
print(f"x is {x}")