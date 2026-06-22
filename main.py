from core.parser import Parser

parser = Parser()

while True:
    user_input = input("You > ")

    result = parser.parse(user_input)

    print(result)

    if result["intent"] == "exit":
        print("Goodbye sir!")
        break