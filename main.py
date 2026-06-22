while True:
    user_input = input("You > ")

    if user_input.lower() == "exit":
        print("Jarvis > Goodbye sir.")
        break

    print("Jarvis > I heard:", user_input)