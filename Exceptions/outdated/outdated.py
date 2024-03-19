months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", 
          "December"]

while True:
    user_input = input("Date: ")
    try:
        # Check which of the formats user input
        if "/" in user_input:
            user_input = user_input.replace(" ", "") 
            month, day, year = user_input.split("/")
        elif ", " in user_input:
            user_input = user_input.replace(",", "")
            month, day, year = user_input.split(" ")
            if month in months:
                month = months.index(month) + 1
        else:
            continue
        
        # Now include the conditions
        if int(day) > 31 or int(month)  > 12:
            pass
        else:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except ValueError:
        pass