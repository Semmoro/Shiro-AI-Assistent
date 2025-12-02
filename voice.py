import pyttsx3
# from ears import intrebareeMea

Voice = pyttsx3.init()

def shiro_response(response):

    print("vocea so gruzit")
    print("Shiro:",response)  
    Voice.say(response)      
    Voice.runAndWait()