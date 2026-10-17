from ddgs import DDGS
import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init()

        engine.setProperty('rate', 230)

        text = str(text)

        print("\nJarvis:", text)

        engine.say(text)

        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print("Speech Error:", e)

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=1))

        if results:
            answer = results[0]["body"]

            if len(answer) > 150:
                answer = answer[:150]

            return answer

        return "Sorry, I could not find any information."

    except Exception as e:
        return f"Search error: {e}"

# Welcome Message
speak("Hello, I am Jarvis. How may I help you?")

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit", "bye"]:
        speak("Goodbye")
        break

    answer = search_web(question)

    print("\nAnswer Found:", answer)

    speak(answer)