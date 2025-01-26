import pyttsx3
import speech_recognition as sr

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Set speaking speed

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input via microphone and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            speak("There seems to be an issue with the speech service.")
            return None

def main():
    """Main function to run TRIOS."""
    speak("Hello! I am TRIOS, your personal assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "your name" in command:
                speak("My name is TRIOS, your personal assistant.")
            elif "how are you" in command:
                speak("I am just a program, but thank you for asking. How can I assist you?")
            elif "exit" in command or "stop" in command:
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("I can only respond to basic commands right now. Please try asking something else.")
        else:
            # If command is None, continue listening
            continue

if __name__ == "__main__":
    main()
