class Executor:

    def execute(self, data):
        intent = data["intent"]

        if intent == "open_app":
            return f"Opening {data['target']}..."
        
        elif intent == "search_web":
            return f"Searching the web for {data['target']}..."
        
        elif intent == "play_music":
            return f"Playing {data['target']}..."
        
        elif intent == "unknown":
            return "I'm sorry, I didn't understand that command."
        
        elif intent == "exit":
            return "Goodbye sir!"
        