def main():
    name = input("What's the camelCase name? ")
    print(convert(name))


def convert(name):
    snake_case = ""
    for i in range(len(name)):
        if name[i].isupper():
            snake_case = '_' + name[i].lower()
        else:
            snake_case += name[i]
    print(snake_case)


main()
