amount = 50
while True:
    print("Amount Due:", amount)
    cash = int(input("Insert Coin: "))
    if cash in [5, 10, 25]:
        amount -= cash
        if amount > 0:
            continue
        else:
            break

print("Change Owed:", abs(amount))


# Or this inefficient one
amount = 50
print("Amount Due:", amount)
while True:
    cash = int(input("Insert Coin: "))
    if cash in [5, 10, 25]:
        amount -= cash
        if amount > 0:
            print("Amount Due:", amount)
        elif amount == 0:
            print("Change Owed: 0")
            break
        else:
            print("Change Owed:", abs(amount))
            break
    else:
        print("Amount Due:", amount)
        continue


# Or this efficient one
amount = 50
while amount > 0:
    print("Amount Due:", amount)
    cash = int(input("Insert Coin: "))
    if cash in [5, 10, 25]:
        amount -= cash

print("Change Owed:", abs(amount))