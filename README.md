# Jarvis Virtual Assistant

A Python-based virtual assistant that retrieves information from the internet and provides spoken responses using text-to-speech technology.

## Features

- Searches the web using DuckDuckGo Search
- Converts search results into speech
- Accepts user questions through keyboard input
- Provides short, relevant responses
- Works without paid AI APIs
- Supports continuous interaction until the user exits

## Technologies Used

- Python
- DDGS (DuckDuckGo Search)
- pyttsx3 (Text-to-Speech)

## Installation

1. Clone the repository.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Run the application:

   `python ai_chatbot.py`

## How It Works

1. The user enters a question.
2. Jarvis searches the internet using DDGS.
3. It retrieves a relevant search result.
4. The text-to-speech engine converts the result into spoken audio.
5. Jarvis speaks the answer through the computer's speakers.

## Limitations

- Requires an internet connection for web searches.
- Currently supports keyboard input rather than microphone input.
- Search results are not independently fact-checked.
- Does not use a large language model.

## Future Improvements

- Voice command recognition
- Reminder and task management
- Weather information
- Application automation
- Graphical user interface

## Author

M Sumaiya