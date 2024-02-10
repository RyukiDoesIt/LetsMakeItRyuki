def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum():
        for letter in s:
            if letter.isdigit():
                num = s.index(letter)
                if s[num:].isdigit() and int(s[num]) != 0:
                    return True
                else:
                    return False
        return True
    else:
        return False


main()