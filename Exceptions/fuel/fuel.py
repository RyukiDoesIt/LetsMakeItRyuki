def main():
    percentage()

def percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            a, b = fraction.split("/")
            ans = int(round((100*(int(a) / int(b)))))
            if 95 < ans <= 100:
                print("F")
                break
            elif ans < 10:
                print("E")
                break
            elif ans > 100:
                pass
            else:
                print(f"{ans}%")
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except NameError:
            pass

if __name__ == "__main__":
    main()
