import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None

def main():
    speak("Hello, I am your voice assistant.")
    while True:
        command = listen()
        if command:
            # Process commands
            if "exit" in command:
                speak("Goodbye!")
                break
            

if __name__ == "__main__":
    main()
