user = input("Expression: ")
x, y, z = user.split(" ")
 
match y:
    case '+':
        answer = float(x) + float(z)
    case '-':
        answer = float(x) - float(z)
    case '*':
        answer = float(x) * float(z)
    case '/':
        answer = float(x) / float(z)

print(answer)
