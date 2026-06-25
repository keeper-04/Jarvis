class Executor:

    def execute(self, data):
        intent = data["intent"]

        if intent == "open_app":
            from commands.open_app import run
            return run(data['target'])
        
        elif intent == "search_web":
            from commands.search_web import run
            return run(data['target'])
        
        elif intent == "play_music":
            return f"Playing {data['target']}..."
        
        elif intent == "get_time":
            from commands.get_time import run
            return f"The current time is: {run()}"
        
        elif intent == "unknown":
            return "I'm sorry, I didn't understand that command."
        
        elif intent == "exit":
            return "Goodbye sir!"
        