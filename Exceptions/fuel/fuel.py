while True:
    # Trying the code
    try:
        # Taking input
        x = int(input("What's x? "))
        # If ValueError is False
        break
    except ValueError:
        # If ValueError is True
        print("x is not an integer!")
    
# Print the variable
print(f"x is {x}")
