
import sounddevice as sd
import queue
import json
import os
from vosk import Model, KaldiRecognizer
from gpt4all import GPT4All
import pyttsx3
from prompt import my_prompt

brain = GPT4All("./Phi-3-mini-4k-instruct-q4.gguf", model_path=".", device="cpu")

voice = Model("./vosk-model-small")
rec = KaldiRecognizer(voice, 16000)
tts = pyttsx3.init()

memories = "Data_Base.json"
memories_DATA = []
q = queue.Queue()

if os.path.exists(memories):
    with open(memories, "r") as f:
        try:
            memories_DATA = json.load(f)
        except json.JSONDecodeError:
            memories_DATA = []


def add_memories(user_text, response):

        memories_DATA.append({"Eu": user_text , "Shiro": response})
        with open(memories, "w") as f:
            json.dump(memories_DATA , f, ensure_ascii= False, indent = 2)

def remove_last_memory():

        memories_DATA.pop()
        with open(memories, "w") as f:
            json.dump(memories_DATA, f, ensure_ascii= False, indent = 2)

def shiro_response(response):
    
    print("✅ Модель загружена на CPU")
    print("Shiro:",response)  
    tts.say(response)      
    tts.runAndWait()

def callback(indata, frames, time_, status):
    q.put(bytes(indata))

with brain.chat_session(system_prompt=my_prompt):

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                user_text = result.get("text", "").strip()

                if not user_text:
                    continue

                print(f"👂 Shiro услышала: {user_text}")

                if user_text.lower() in ["спи", "sleep"]:
                    tts.say('OK Nii good by')
                    tts.runAndWait()
                    break

                elif user_text.lower() in [ "remove last memory"]:
                    remove_last_memory()
                    tts.say('What, wich memory?')
                    tts.runAndWait()

                else:
                    response = brain.generate(user_say, max_tokens = 10)  
                    shiro_response()
                    add_memories()

