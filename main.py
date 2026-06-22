from core.parser import Parser
from core.executor import Executor

parser = Parser()
executor = Executor()

while True:
    user_input = input("You > ")

    result = parser.parse(user_input)

    response = executor.execute(result)
    print("Jarvis >", response)

    if result["intent"] == "exit":
        break