import pyttsx3

Voice = pyttsx3.init()

def shiro_response(response):

    print("✅ Модель загружена на CPU")
    print("Shiro:",response)  
    Voice.say(response)      
    Voice.runAndWait()