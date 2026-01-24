###🤖 AI Chatbot Development using Groq API in Python

This project demonstrates how to build a ChatGPT-style AI chatbot in Python using the Groq AI API.
The chatbot accepts user input from the console and streams AI-generated responses in real time, similar to ChatGPT.

##🚀 Features

Interactive command-line chatbot

Real-time streaming responses (word-by-word)

Uses Groq’s LLaMA-3.1-8B-Instant model

Simple and beginner-friendly Python implementation

Exit commands supported (quit, exit, bye)

##🧠 What You’ll Learn

How to set up and use the Groq API in Python

Sending user prompts to an AI model

Streaming AI responses in real time

Building a basic conversational AI application

##🛠️ Tech Stack

Python

Groq AI API

LLaMA 3.1 (8B Instant Model)

##📦 Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-link>
cd your-project-folder

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install groq

🔑 API Key Setup

Create a Groq API key from the Groq platform and update it in the code:

client = Groq(api_key="YOUR_API_KEY")


⚠️ Never share your API key publicly.
(For production, use environment variables.)

▶️ How to Run
python chatbot.py

##💬 Usage

Type your message and press Enter

The chatbot will respond in real time

Type quit, exit, or bye to end the conversation

##📌 Example
You: Explain machine learning
Chatbot: Machine learning is a field of artificial intelligence...

##🎯 Use Cases

Beginner AI/ML projects

Learning API integration in Python

Understanding real-time response streaming

Resume and portfolio projects
