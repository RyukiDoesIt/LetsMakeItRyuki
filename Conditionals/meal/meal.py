def main():
    time_user = input("What's the time? ")
    time = convert(time_user)
    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print("")

def convert(time):
    H, M = map(float, time.split(":"))
    total = H + M / 60
    return total

if __name__ == "__main__":
    main()
