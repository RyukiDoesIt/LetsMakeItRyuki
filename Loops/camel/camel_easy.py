camel = input("type camelCase: ")
print("snake_case: ", end='')

for alpha in camel:
    if alpha.isupper():
        print("_" + alpha.lower(), end='')
    else:
        print(alpha, end='')
print()