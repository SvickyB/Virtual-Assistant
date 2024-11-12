### README

# Virtual Assistant Project (Jarvis)

This is a Python-based **Virtual Assistant** that can perform various tasks through voice commands. It leverages popular libraries such as **pyttsx3**, **speech_recognition**, **wikipedia**, and **pywhatkit** to provide functionality like searching Wikipedia, playing songs, sending emails, and more.

The assistant responds to various voice commands and performs a variety of tasks, such as telling the time, checking system battery, sending emails, playing music, searching the web, and many more.

## Features
- **Voice Interaction**: The assistant uses speech recognition and text-to-speech to interact with the user.
- **Weather Information**: The assistant can fetch the current temperature for any location.
- **Web Search**: It can search Google and Wikipedia based on voice input.
- **Music Control**: It can play songs via YouTube or local files.
- **Email Sending**: It can send emails using Gmail.
- **Battery Status**: It informs you of the current battery percentage of your system.
- **Mathematical Calculations**: It can perform basic arithmetic calculations.
- **Social Media Access**: Open Instagram, WhatsApp, and other websites via voice commands.
- **Open Apps**: It can open applications like Google Chrome, VS Code, etc.

## Requirements

- Python 3.x
- Libraries:
  - `pyttsx3`: For text-to-speech functionality.
  - `speech_recognition`: For speech recognition from the microphone.
  - `wikipedia`: For querying Wikipedia.
  - `pywhatkit`: For playing songs on YouTube and searching on Google.
  - `requests`: For making HTTP requests to fetch data from websites (e.g., weather).
  - `psutil`: For monitoring system battery and other system metrics.
  - `beautifulsoup4`: For web scraping (used in weather search).

You can install the necessary libraries by running the following commands:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pywhatkit
pip install requests
pip install psutil
pip install beautifulsoup4
```

## Usage

### 1. **Voice Commands**:
Once you start the program, it will begin listening for voice commands. Some common voice commands include:
- "What is the time?"
- "Search for [topic] on Wikipedia."
- "Play [song] on YouTube."
- "Send an email."
- "Open [application or website]."
- "How much power is left?"

### 2. **Tasks Performed**:
- **Greeting**: The assistant will greet you according to the time of the day.
- **Weather**: "Temperature in [location]" will fetch the current temperature of the location.
- **Email**: You can send emails by voice command. Just tell the assistant what message you want to send.
- **Music**: You can play music from YouTube or a local directory.
- **System Information**: Get the battery percentage and other system-related information.
- **Opening Applications**: The assistant can open various applications like Google Chrome, VS Code, Gmail, WhatsApp, and more.

### 3. **Example Interaction**:
- **User**: "What is the time?"
- **Assistant**: "The time is [current time]."
  
- **User**: "Search for Python programming on Wikipedia."
- **Assistant**: "Searching Wikipedia... According to Wikipedia, Python is a high-level programming language."

- **User**: "Play music."
- **Assistant**: "Playing music for you."

## Code Walkthrough

- **Initialization**: The assistant is initialized using `pyttsx3.init()` for speech synthesis and `speech_recognition` for recognizing commands from the microphone.
- **Command Execution**: The assistant listens to the user's voice, processes the command, and executes the corresponding task (e.g., opening a website, playing a song, sending an email).
- **Weather**: For weather information, the assistant scrapes data from Google using `requests` and `BeautifulSoup`.
- **Email Sending**: The assistant can send emails using the SMTP protocol by logging into your Gmail account.
- **Mathematics**: The assistant can process basic arithmetic expressions and return the result.

## Important Notes

- Make sure to update the **email credentials** in the `mail()` function to your own Gmail account details for the email functionality to work.
- **Microphone and Internet Connection**: Ensure you have a working microphone for voice input and an active internet connection for web searches and playing music.
- The program runs in a continuous loop and listens for commands until the user stops it.

## Contributing

Feel free to fork this repository, open issues, and submit pull requests if you'd like to contribute new features, fix bugs, or improve the code.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Let me know if you need further details or assistance!
