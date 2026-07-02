import json
import os

class Memory:

    def __init__(self):
        self.file_path = "data/memory.json"
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.memory = {}
        self.load_memory()

    def load_memory(self):
        try:
            with open(self.file_path, "r") as file:
                self.memory = json.load(file)
        except FileNotFoundError:
            self.memory = {}
        except json.JSONDecodeError:
            self.memory = {}
    
    def save_memory(self):
        with open(self.file_path, "w") as file:
            json.dump(self.memory, file, indent=4)

    def remember(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def forget(self, key):
        if key in self.memory:
            del self.memory[key]
            self.save_memory()

    def recall(self, key):
        return self.memory.get(key, None)