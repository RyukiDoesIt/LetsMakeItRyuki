# Define main which takes input and assign to variable
def main():
    print(change(input("Give emoji: ")))

# Define the function which change emoticons to emojies
def change(emoticons):
    smiley = emoticons.replace(":)", "🙂").replace(":(", "🙁")
    return smiley

# Call main
main()