def main():
    greet = input("Greeting: ")
    greet = greet.lower().lstrip()
    if greet.startswith("hello"):
        print("$0")
    elif with_h(greet):
        print("$20")
    else:
        print("$100")

def with_h(user):
    return True if user.startswith("h") else False

main()
