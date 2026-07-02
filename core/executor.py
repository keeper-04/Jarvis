class Executor:

    def execute(self, data, memory):
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
        
        elif intent == "remember":
            memory.remember(data['key'], data['value'])
            return f"Okay i will remember that your {data['key']} is {data['value']} sir."
        
        elif intent == "recall":
            value = memory.recall(data['key'])
            if value:
                return f"Your {data['key']} is {value} sir."
            else:
                return f"I don't remember anything about {data['key']}."
            
        elif intent == "forget":
            memory.forget(data['key'])
            return f"I have forgotten {data['key']}."
        
        elif intent == "unknown":
            return "I'm sorry, I didn't understand that command."
        
        elif intent == "exit":
            return "Goodbye sir!"
        