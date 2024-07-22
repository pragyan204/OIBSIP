import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initializing the speech recognition and text-to-speech engine
listener = sr.Recognizer()
speech_engine = pyttsx3.init()

def speak_text(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

def capture_audio():
    with sr.Microphone() as mic_source:
        print("Awaiting your command...")
        audio_data = listener.listen(mic_source)
        try:
            user_input = listener.recognize_google(audio_data)
            print(f"Captured: {user_input}\n")
        except sr.UnknownValueError:
            speak_text("Apologies, I didn't catch that.")
            user_input = None
        return user_input

def handle_command(command):
    if command is None:
        return

    command = command.lower()

    if "hello" in command:
        speak_text("Greetings! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak_text(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak_text(f"Today's date is {current_date}")
    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(search_url)
            speak_text(f"Displaying search results for {search_term}")
        else:
            speak_text("What would you like to search for?")
    else:
        speak_text("I'm sorry, I didn't understand that. Could you please repeat?")

def initiate_assistant():
    speak_text("Voice assistant activated. How can I help you?")
    while True:
        user_command = capture_audio()
        handle_command(user_command)

if __name__ == "__main__":
    initiate_assistant()