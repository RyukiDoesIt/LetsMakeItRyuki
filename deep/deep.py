answer = input("What is the answer to the question of Life, the Universe and Everything? ")
answer = answer.lower().replace(" ", "")

match answer:
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
