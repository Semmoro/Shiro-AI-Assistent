from vosk import KaldiRecognizer, Model
import sounddevice as sd
import  json

intrebareeMea = ""
previous_element = intrebareeMea


print("modelu de voce se incarca")
# model = Model("vosk-model-ru-0.42") --Modelu mai mare nu de udali!!!!!1
model = Model("vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 16000)


def callback(indata, frames, time_info, status):
    global intrebareeMea, previous_element

    data = bytes(indata)
    if rec.AcceptWaveform(data):
        rezultatul = json.loads(rec.Result())
        text = rezultatul.get("text", "")
        print("Rezultat:", text)

        if "ассистент" in text:
            intrebareeMea = text

    else:
        rezPartial = json.loads(rec.PartialResult())
        print("Rez. partial:", rezPartial)

def listen():
    global intrebareeMea
    intrebareeMea = "" 

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("ascult, vorbeste:")

        sd.sleep(6000)
        print(intrebareeMea)










