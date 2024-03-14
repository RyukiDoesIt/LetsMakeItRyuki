counts = {}

# The infinite loop
while True:
    try:
        name = input().upper()
    except EOFError:
        print()
        break
    except KeyError:
        pass
    if name not in counts:
        counts[name] = 1 # Assigns value of 1
    else:
        counts[name] += 1 # Increments value with 1

# The sorting procedure
keys = sorted(counts.keys())
Sorted = {}

# The printing
for key in keys:
    Sorted[key] = counts[key] # Assigns previous values to sorted ones
    print(Sorted[key], key)