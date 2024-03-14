grocery_list = []
counts = {}

while True:
    try:
        name = input()
        grocery_list.append(name.upper())
    except EOFError:
        print()
        break
    except KeyError:
        pass

for items in grocery_list:
    if items not in counts:
        counts[items] = 1
    else:
        counts[items] += 1

for item, count in counts.items():
    print(count, item)