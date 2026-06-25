class Parser:

    def parse(self, command):
        command = command.lower().strip()
        words = command.split()

        if(len(words) == 0):
            return {
                "intent": "unknown"
            }
        
        action = words[0]

        if action == "open":
            return {
                "intent": "open_app",
                "target": " ".join(words[1:])
            }
        elif action == "search":
            return {
                "intent": "search_web",
                "target": " ".join(words[1:])
            }
        elif action =="exit":
            return {
                "intent": "exit"
            }
        elif action == "play":
            return {
                "intent": "play_music",
                "target": " ".join(words[1:])
            }
        elif action == "time":
            return {
                "intent": "get_time"
            }
        else:
            return {
                "intent": "unknown"
            }