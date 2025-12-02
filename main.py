from brain import Brain
from memory import *
from prompt import my_prompt
from voice import Voice, shiro_response
import ears


with Brain.chat_session(system_prompt=my_prompt):


    while True:
        createTable()

        ears.listen()

            
        if ears.intrebareeMea == "ассистент спи":
            Voice.say('OK, до встречи')
            Voice.runAndWait()
            break

        elif ears.intrebareeMea == "ассистент забудь об этом воспоминаний":
            deleteTable()
            Voice.say('что ты о чём?')
            Voice.runAndWait()
                
        else:
            response = Brain.generate(ears.intrebareeMea)  
            shiro_response(response)
            updateTable(ears.intrebareeMea, response)



