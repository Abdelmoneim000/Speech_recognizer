import speech_recognition as sr
import pyttsx3
from vosk import Model, KaldiRecognizer
import os
import json

# Initialize the text-to-speech engine
engine = pyttsx3.init()
model_path = "vosk-model-en-us-0.42-gigaspeech"  # Path to the language model

# Example texts
texts = {
    "Gettysburg Address": "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal",
    # Add more texts here
}

def speak(text):
    """Speak out the text using TTS."""
    engine.say(text)
    engine.runAndWait()

def listen_and_recognize():
    """Listen to the user's recitation and attempt to recognize the speech using Vosk for offline recognition."""
    if not os.path.exists(model_path):
        print("Model path is incorrect or the model is not downloaded. Please check the model path.") # If the model is not downloaded, download it from https://alphacephei.com/vosk/models and extract it to the current directory
        exit(1)
    model = Model(model_path)
    # Initialize the recognizer with the model
    recognizer = KaldiRecognizer(model, 16000)

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...") # Once you see this message, Start talking
        audio = sr.Recognizer().listen(source)
        audio_data = audio.get_wav_data()
        print(f"Audio data length: {len(audio_data)}") # For debugging, Making sure that the mic is working and audio is being recorded.
        
        if recognizer.AcceptWaveform(audio_data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            print(f"Recognized: {text}")  # For debugging, phrase recognized by the recognizer.
            return text
        else:
            print("Sorry, I could not understand the audio.")
            return None

def compare_texts(recited, reference):
    """Compare recited text to the reference, return index of first mistake or -1 if perfect."""
    recited_words = recited.split()
    reference_words = reference.split()
    for i, (recited_word, reference_word) in enumerate(zip(recited_words, reference_words)):
        if recited_word.lower() != reference_word.lower():
            return i
    return -1

def main():
    # Example usage
    text_choice = "Gettysburg Address"  # This could be made dynamic
    reference_text = texts[text_choice]
    
    speak(f"{text_choice}, begin:")
    
    recited_text = listen_and_recognize()
    if recited_text:
        mistake_index = compare_texts(recited_text, reference_text)
        if mistake_index == -1:
            speak("Perfect recitation!")
        else:
            speak(f"Mistake detected at word {mistake_index + 1}. Try again from: {' '.join(reference_text.split()[:mistake_index][-3:])}")

if __name__ == "__main__":
    main()
