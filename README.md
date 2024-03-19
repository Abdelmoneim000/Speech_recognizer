## Offline speech recognizer

### Set up the project :

 1. download the required libraries using the following command:
 
    `pip install -r requirements.txt`
 
 2. install the required language model form [This link](https://alphacephei.com/vosk/models)
 
 4. unzip the model in the same working directory to be exactly like this :

    ```bash
    .
    ├── main.py
    ├── vosk-model-en-us-042-gigaspeech # The language model.
    └── README.md
    ```
 5. once you installed the required model, update the following line in main.py:
     
    ```python
    model_path = "vosk-model-en-us-0.42-gigaspeech"  # Path to the language model
    ```

### Run the program:
    
 1. run the following command:
     
    ```bash
    python main.py
    ```
     
 2. the program will print some logs to the console, setting up the recognizer and the microphone.

 3. once you see the final log `Listening...`, you can start speaking and the program will print the recognized text to the console.

 4. after you finish your speech, wait to see what the program recognized, the program will print the audio length and the recognized text.

 5. if the program couldn't recognize the speech, it will print `Sorry, I couldn't understand the audio.` meaning that the audio was not clear enough to be recognized. try to speak louder and clearer.

------

Right now, the program is only for testing purposes, and only runs in the console and captures the audio once then closes again. I'm planning to make it run in the background and capture the audio continuously, and also to make it recognize the audio in real-time.

