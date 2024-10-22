import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return command
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return None

# Function to process commands
def process_command(command):
    if "hello" in command.lower():
        speak("Hello! How can I assist you today?")
    elif "time" in command.lower():
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif "date" in command.lower():
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command.lower():
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
    else:
        speak("I didn't catch that. Could you say it again?")

# Main loop
def main():
    speak("Voice Assistant activated. Say something!")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)
        if "exit" in command.lower():
            speak("Goodbye!")
            break

# Run the assistant
if __name__ == "__main__":
    main()
