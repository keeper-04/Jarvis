from datetime import datetime

class Logger:

    def log(self, command):

        with open("logs/jarvis.log", "a") as file:
            file.write(
                f"{datetime.now()} - {command}\n"
            )