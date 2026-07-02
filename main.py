from core.parser import Parser
from core.executor import Executor
from core.logger import Logger
from core.memory import Memory

parser = Parser()
executor = Executor()
logger = Logger()
memory = Memory()

while True:
    user_input = input("You > ")
    logger.log(user_input)

    result = parser.parse(user_input)

    response = executor.execute(result, memory)
    print("Jarvis >", response)

    if result["intent"] == "exit":
        break