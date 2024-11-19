# Import necessary modules
import speech_recognition as sr  # For converting speech into text
import pyttsx3  # For converting text into speech
from datetime import datetime, date  # For time and date

# Initialize the text-to-speech engine/module and assign it to text_to_speech variaable
text_to_speech = pyttsx3.init()

def say_something(message):
    text_to_speech.say(message)  # This method queues the string (message) to be spoken.
    text_to_speech.runAndWait()  # This method processes and plays the queued speech commands.

def capture_voice():
    # Listens to the user's voice through the microphone and converts it into text..
    recognizer = sr.Recognizer()  # Create an instance of the speech recognizer
    with sr.Microphone() as mic:  # Use the microphone as the input device
        print("I'm listening...")  # Inform the user that the assistant is ready to listen
        recognizer.adjust_for_ambient_noise(mic)  # for background noise reduction 
        try:
            # Listen to the audio input for up to 5 seconds
            audio_data = recognizer.listen(mic, timeout=5)
            print("Processing what you said...")  # Inform the user that recognition is in progress
            voice_text = recognizer.recognize_google(audio_data)  # Convert the audio to text using Google's recognition service
            return voice_text.lower()  # Return the recognized text in lowercase
        except sr.UnknownValueError:
            # If speech is unclear or unrecognized
            say_something("I couldn't understand you. Can you please repeat?")
            return None
        except sr.RequestError:
            # If there's an issue with the recognition service
            say_something("There seems to be an issue with the recognition service.")
            return None
        
 #the main method where to listen to the commands ,process them and response them by the VA
def assistant_main():
    say_something("Hi there! I'm ready to assist you. What can I do for you?")  # Initial greeting
    
    while True:  # Keep listening for commands until the user exits
        user_command = capture_voice()  # Capture the user's spoken command
        
        if user_command:  # If a valid command was captured
            print(f"You said: {user_command}")  # Print the command for reference
            
            # Respond to specific commands
            if "hi" in user_command or "hello" in user_command:
                say_something("Hello! How are you doing?")  # Respond to a greeting
            elif "your name" in user_command:
                say_something("I am your voice assistant. Nice to meet you!")  # Introduce itself
            elif "time" in user_command:
                # Get the current time and format it (e.g., 03:45 PM)
                current_time = datetime.now().strftime("%I:%M %p")
                say_something(f"The current time is {current_time}.")  # Inform the user of the time
            elif "date" in user_command:
                # Get today's date and format it
                today_date = date.today().strftime("%B %d, %Y")
                say_something(f"Today's date is {today_date}.")
            elif "stop" in user_command or "bye" in user_command:
                # Exit the assistant when the user says "stop" or "bye"
                say_something("Alright, goodbye! Have a great day!")
                break  # Exit the loop, ending the assistant
            else:
                # If the assistant doesn't recognize the command
                say_something("I'm not sure how to help with that yet.")

# Run the assistant when the script is executed directly
if __name__ == "__main__":
    assistant_main()  # Start the assistant

# This is the voice generated output as you see on the console
