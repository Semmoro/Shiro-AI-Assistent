import json
import os 

memories = "Data_Base.json" 
memories_DATA = []


if os.path.exists(memories):
    with open(memories, "r") as f:
        try:
            memories_DATA = json.load(f)

        except json.JSONDecodeError:
                memories_DATA = []
else:
    memories_DATA = []

def remove_last_memory():
    global memories_DATA
    if memories_DATA:            
        memories_DATA.pop()
        with open(memories, "w") as f:
            json.dump(memories_DATA, f, ensure_ascii= False, indent = 2)

def add_memories(user_say, response):
    global memories_DATA

    memories_DATA.append({"Eu": user_say , "Shiro": response})
    with open(memories, "w") as f:
        json.dump(memories_DATA , f, ensure_ascii= False, indent = 2)