def main():
    name = input("Type camelCase: ")
    convert(name)

def convert(user_in):
    changed_name = ""
    for i in range(len(user_in)):
        if user_in[i].isupper():
            changed_name = changed_name + '_' + user_in[i].lower()
        else:
            changed_name += user_in[i]
    print("snake_case:", changed_name)    

main()