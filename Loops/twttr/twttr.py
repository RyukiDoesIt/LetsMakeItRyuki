name = input("Input: ")

print("Output: ", end="")
for letter in name:
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        letter = ""
        print(letter, end="")
    else:
        print(letter, end="")

print()