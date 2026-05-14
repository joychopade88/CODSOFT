import re
import random
from datetime import datetime

RULES = [
    {
        "pattern": r"hi|hello|hey|howdy",
        "responses": [
            "Hello! How can I help you? 😊",
            "Hey there! What's up?",
            "Hi! Ask me anything!"
        ]
    },
    {
        "pattern": r"how are you|how r u|how's it going",
        "responses": [
            "I'm just a bot, but I'm doing great!",
            "All systems running! How about you?"
        ]
    },
    {
        "pattern": r"your name|who are you|what are you",
        "responses": [
            "I'm ChatBot, built for the CodSoft AI internship! 🤖",
            "I'm an AI chatbot written in Python."
        ]
    },
    {
        "pattern": r"joke|funny|make me laugh",
        "responses": [
            "Why don't scientists trust atoms? They make up everything! 😂",
            "Why did the programmer quit? He didn't get arrays! 🤣",
            "A SQL query walks into a bar and asks two tables: 'Can I JOIN you?' 😄"
        ]
    },
    {
        "pattern": r"time|current time",
        "responses": [f"The current time is {datetime.now().strftime('%I:%M %p')} ⏰"]
    },
    {
        "pattern": r"date|today|what day",
        "responses": [f"Today is {datetime.now().strftime('%A, %d %B %Y')} 📅"]
    },
    {
        "pattern": r"weather|temperature",
        "responses": ["I can't check live weather, but try Google! 🌤️"]
    },
    {
        "pattern": r"thanks|thank you|thx",
        "responses": ["You're welcome! 😊", "Happy to help!"]
    },
    {
        "pattern": r"bye|goodbye|exit|quit",
        "responses": ["Goodbye! Have a great day! 👋", "See you later! 😊"]
    },
]

FALLBACK = [
    "Hmm, I didn't get that. Could you rephrase?",
    "I'm not sure what you mean. Try asking something else!",
    "That's beyond my current rules. 🤔"
]

def get_response(user_input):
    text = user_input.lower().strip()
    for rule in RULES:
        if re.search(rule["pattern"], text):
            return random.choice(rule["responses"])
    return random.choice(FALLBACK)

def main():
    print("🤖 ChatBot — CodSoft AI Task 1")
    print("Type 'bye' to exit\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        response = get_response(user_input)
        print(f"ChatBot: {response}\n")
        if re.search(r"bye|exit|quit", user_input.lower()):
            break

if __name__ == "__main__":
    main()