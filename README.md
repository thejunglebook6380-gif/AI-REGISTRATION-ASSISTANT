AI Registration Assistant

Task Information

Task ID: AI-SS-001
Project Name: AI Registration Assistant
Domain: Student Support & Internship Management NLP
Technology Stack: Python, NLTK, NLP, Regular Expressions, JSON

Project Overview

The AI Registration Assistant is a Python-based conversational chatbot designed to guide students through an internship registration process.

The chatbot interacts with users, collects registration information, validates programming experience, and stores registration records locally in a JSON file.

Objectives

- Implement basic Natural Language Processing.
- Recognize user intents.
- Extract student information such as name and email.
- Create a conversational registration flow.
- Validate user inputs.
- Store registration information using JSON.

Technologies Used

- Python
- NLTK
- Natural Language Processing
- Regular Expressions
- JSON
- Rule-based Intent Classification

Features

- Greeting and introduction
- Registration assistance
- Help and support responses
- Internship-related FAQ responses
- Name extraction
- Email extraction
- Field of study collection
- Programming experience validation
- Registration confirmation
- JSON-based data storage
- Support for multiple registration records

NLP Implementation

The project uses NLTK for text preprocessing.

The preprocessing process includes:

1. Converting user input to lowercase.
2. Tokenizing the input.
3. Removing stop words.
4. Lemmatizing words.

The chatbot then compares the processed user input with predefined intent patterns stored in "intents.json".

Entity Extraction

Regular expressions are used to extract:

- Student name
- Email address

The extracted information is stored in a Python dictionary before being saved locally.

Registration Workflow

The chatbot follows this conversation flow:

Name → Email → Field of Study → Programming Experience → Registration Confirmation

After successful registration, the information is saved locally in:

registration_data.json

This generated file is excluded from the GitHub repository to avoid exposing registration information.

Project Structure

AI-REGISTRATION-ASSISTANT/
│
├── app.py
├── chatbot.py
├── chatbot2.py
├── intents.json
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

How to Run

1. Clone the repository

git clone https://github.com/thejunglebook6380-gif/AI-REGISTRATION-ASSISTANT.git

2. Open the project folder

cd AI-REGISTRATION-ASSISTANT

3. Install the required packages

pip install -r requirements.txt

4. Run the chatbot

python chatbot2.py

Project Status

Completed — AI Registration Assistant

Developed as part of the AI & Data Science internship project.