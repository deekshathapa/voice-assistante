import asyncio
import websockets
import datetime
import random
import os

async def handle_client(websocket):
    async for message in websocket:
        msg = message.lower().strip()
        print("User said:", msg)

        response = "Sorry, I didn't understand that."

        # Greetings
        if "hello" in msg or "hi" in msg:
            response = "Hello! How can I help you today?"

        elif "how are you" in msg:
            response = "I'm doing great. How can I assist you?"

        elif "your name" in msg:
            response = "I am Vox AI, your voice assistant."

        # Time
        elif "time" in msg:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {now}"

        # Date
        elif "date" in msg:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            response = f"Today's date is {today}"

        # Google search
        elif msg.startswith("search "):
            query = msg.replace("search", "").strip()
            response = f"OPEN::https://www.google.com/search?q={query}"

        # YouTube search
        elif msg.startswith("youtube search"):
            query = msg.replace("youtube search", "").strip()
            response = f"OPEN::https://www.youtube.com/results?search_query={query}"

        # Open sites
        elif "open youtube" in msg:
            response = "OPEN::https://www.youtube.com"

        elif "open google" in msg:
            response = "OPEN::https://www.google.com"

        elif "open facebook" in msg:
            response = "OPEN::https://www.facebook.com"

        elif "open twitter" in msg:
            response = "OPEN::https://www.twitter.com"

        # Wikipedia
        elif "wikipedia" in msg:
            query = msg.replace("wikipedia", "").strip()
            if query:
                response = f"OPEN::https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
            else:
                response = "OPEN::https://en.wikipedia.org"

        # News
        elif "news" in msg or "open news" in msg:
            response = "OPEN::https://news.google.com"

        # Weather
        elif "weather" in msg:
            response = "OPEN::https://www.google.com/search?q=weather"

        # Calculator
        elif msg.startswith("calculate "):
            try:
                expression = msg.replace("calculate", "").strip()
                result = eval(expression)
                response = f"The result is {result}"
            except:
                response = "Sorry, I couldn't calculate that."

        # Joke
        elif "joke" in msg:
            jokes = [
                "Why don’t programmers like nature? Too many bugs.",
                "Why did the computer show up at work late? It had a hard drive.",
                "Debugging is like being a detective in a crime movie where you are also the murderer."
            ]
            response = random.choice(jokes)

        # Motivation
        elif "motivate" in msg or "quote" in msg or "inspire" in msg:
            quotes = [
                "Push yourself because no one else is going to do it for you.",
                "Dream it. Wish it. Do it.",
                "Great things never come from comfort zones.",
                "Success doesn't just find you. You have to go out and get it."
            ]
            response = random.choice(quotes)

        # Fun facts
        elif "fact" in msg:
            facts = [
                "Honey never spoils.",
                "Octopuses have three hearts.",
                "Bananas are berries but strawberries are not."
            ]
            response = random.choice(facts)

        # Goodbye
        elif "bye" in msg or "goodbye" in msg:
            response = "Goodbye! Have a great day."

        await websocket.send(response)

async def main():
    port = int(os.environ.get("PORT", 8765))
    async with websockets.serve(handle_client, "0.0.0.0", port):
        print(f"Server running on port {port}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())