from brain import Brain
from memory import *
from prompt import my_prompt
from voice import Voice, shiro_response
import ears


with Brain.chat_session(system_prompt=my_prompt):

    while True:
        user_say = input("Eu:")
            
        if user_say == "sleep":
            Voice.say('OK Nii good by')
            Voice.runAndWait()
            break

        elif user_say == "remove last memory":
            remove_last_memory()
            Voice.say('What, wich memory?')
            Voice.runAndWait()
                
        else:
            response = Brain.generate(user_say, max_tokens = 10)  
            shiro_response(response)
            add_memories(user_say, response)



