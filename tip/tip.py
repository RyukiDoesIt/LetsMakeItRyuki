def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars_without_sign = float(dollars.replace("$", ""))
    return dollars_without_sign


def percent_to_float(percentage):
    cut = float(percentage.replace("%", "")) * .01
    return cut

main()
