from gtts import gTTS
import speech_recognition as sr
import os

def recognize_speech(recognizer):
    with sr.Microphone() as source:
        print('Say something...')
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print(f'You said: {text}')
    except sr.UnknownValueError:
        print('Error: Could not understand your speech')
        return None
    except sr.RequestError as e:
        print(f'Error with service; {e}')
        return None
    return text

def say_to_text(text):
    if text:
        tts = gTTS(text=text, lang="ru")
        tts.save('audio_1.mp3')
        os.system('audio_1.mp3')

def main():
    recognizer = sr.Recognizer()
    text = recognize_speech(recognizer)
    if text:
        say_to_text(text)

main()
