def main():
    getOrder()

def getOrder():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    initial = 0
    while True:
        try:
            order = input("Item: ")
            for key in menu:    
                if order.title() == key:
                    initial += float(menu[key])
                    print(f"${initial:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            pass

if __name__ == "__main__":
    main()