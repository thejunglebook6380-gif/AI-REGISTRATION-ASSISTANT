# AI Registration Assistant

## Task Information

**Task ID:** AI-SS-001

**Project Name:** AI Registration Assistant

**Domain:** Student Support & Internship Management NLP

**Technology Stack:** Python, NLTK, NLP, Regular Expressions, JSON

---

## Project Overview

The AI Registration Assistant is a Python-based conversational chatbot
designed to guide students through an internship registration process.

The chatbot interacts with users, collects registration information,
validates the programming experience, and stores the registration data
in a JSON file.

---

## Objectives

- Implement basic Natural Language Processing.
- Recognize user intents.
- Extract user information such as name and email.
- Create a conversational registration flow.
- Validate user inputs.
- Store registration information using JSON.

---

## Technologies Used

- Python
- NLTK
- Natural Language Processing
- Regular Expressions
- JSON
- Rule-based Intent Classification

---

## Features

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
- Multiple registration records

---

## NLP Implementation

The project uses NLTK for text preprocessing.

The preprocessing process includes:

1. Converting text to lowercase.
2. Tokenizing the input.
3. Removing stop words.
4. Lemmatizing words.

The chatbot then compares processed user input with predefined
intent patterns stored in `intents.json`.

---

## Entity Extraction

Regular expressions are used to extract:

- Student name
- Email address

The extracted information is stored in a Python dictionary before
being saved to the JSON file.

---

## Registration Workflow

The chatbot follows this conversation flow:

**Name → Email → Field of Study → Programming Experience → Registration Confirmation**

After successful registration, the information is saved in:

`registration_data.json`

---

## Project Structure

```text
AI-REGISTRATION-ASSISTANT/
│
├── chatbot2.py
├── intents.json
├── registration_data.json
├── requirements.txt
└── README.md