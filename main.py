from core.parser import Parser
from core.executor import Executor
from core.logger import Logger
from core.memory import Memory
from input.keyboard import KeyboardInput
from input.voice import VoiceInput

input = VoiceInput()
parser = Parser()
executor = Executor()
logger = Logger()
memory = Memory()

while True:
    user_input = input.get_input()
    logger.log(user_input)

    result = parser.parse(user_input)

    response = executor.execute(result, memory)
    print("Jarvis >", response)

    if result["intent"] == "exit":
        break