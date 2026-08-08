import json
import re
import random
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class RegistrationAssistant:

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

        with open("intents.json", "r") as file:
            self.intents = json.load(file)["intents"]

        self.user_data = {}

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9@._ ]', '', text)

        words = nltk.word_tokenize(text)

        words = [
            self.lemmatizer.lemmatize(word)
            for word in words
            if word not in self.stop_words
        ]

        return words

    def classify_intent(self, user_input):

        tokens = self.preprocess(user_input)

        for intent in self.intents:
            for pattern in intent["patterns"]:
                pattern_tokens = self.preprocess(pattern)

                if any(word in tokens for word in pattern_tokens):
                    return intent

        return None

    def extract_name(self, text):

        match = re.search(r"(?:my name is|i am|i'm)\s+([A-Za-z ]+)", text, re.I)

        if match:
            return match.group(1).strip()

        return None

    def extract_email(self, text):

        match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

        if match:
            return match.group()

        return None

    def save_registration(self):

        with open("registration_data.json", "w") as file:
            json.dump(self.user_data, file, indent=4)

    def chat(self):

    print("=" * 50)
    print("🤖 AI Registration Assistant")
    print("Type 'exit' anytime to quit")
    print("=" * 50)

    while True:

        user = input("You : ")

        if user.lower() == "exit":
            print("Assistant : Goodbye!")
            break

        name = self.extract_name(user)

        if name:
            self.user_data["Name"] = name
            print(f"Assistant : Nice to meet you, {name}! Please enter your email.")
            continue

        email = self.extract_email(user)

        if email:
            self.user_data["Email"] = email

            field = input("Assistant : Enter your Field of Study: ")
            self.user_data["Field"] = field

            experience = input("Assistant : Enter your Programming Experience (Beginner/Intermediate/Advanced): ")
            self.user_data["Experience"] = experience

            self.save_registration()

            print("\n===== Registration Successful =====")
            print("Name :", self.user_data["Name"])
            print("Email :", self.user_data["Email"])
            print("Field :", self.user_data["Field"])
            print("Experience :", self.user_data["Experience"])
            print("===================================")
            continue

        intent = self.classify_intent(user)

        if intent:
            print("Assistant :", random.choice(intent["responses"]))
        else:
            print("Assistant : Sorry, I didn't understand.")