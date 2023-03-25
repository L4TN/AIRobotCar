from config import filename
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    with sr.AudioFile('audio_file.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language='pt-BR')
    print(f"texto detectado: {text}")
    return text
