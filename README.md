# AI Email Reply Generator

AI Email Reply Generator is a Python-based application that automatically generates professional responses to emails using Google Gemini (Generative AI). The tool reads an incoming email message, understands its intent, and produces a suitable reply.

This project demonstrates how generative AI can be used to automate common business communication tasks such as responding to product inquiries, customer support emails, and general information requests.

---

## Project Overview

In many organizations, employees spend a significant amount of time replying to emails. This project demonstrates how AI can assist in automating that process.

The system works by:

1. Accepting an email message as input.
2. Sending the content to a generative AI model.
3. Analyzing the context and intent of the message.
4. Generating a professional reply automatically.

This type of automation can be useful for:

* Customer support systems
* Product inquiry responses
* Business communication assistance
* Email productivity tools

---

## Features

* Automatic generation of professional email replies
* Uses Google Gemini generative AI model
* Simple web interface built with Streamlit
* Secure API key management using `.env`
* Easy to run locally and deploy online

---

## Technologies Used

The project is built using the following technologies:

* **Python** – Core programming language
* **Streamlit** – Web interface for interacting with the AI
* **Google Generative AI (Gemini API)** – AI model for generating responses
* **python-dotenv** – Secure environment variable management
* **Git & GitHub** – Version control and project hosting

---

## Project Structure

The repository is organized as follows:

```id="c3m2pf"
AI-Email-Reply-Generator
│
├── app.py            # Main Streamlit application
├── requirements.txt  # Project dependencies
├── README.md         # Project documentation
├── .gitignore        # Files ignored by Git
└── .env              # API key (not uploaded to GitHub)
```

---

## Installation

Clone the repository:

```id="lhbqgo"
git clone https://github.com/praneethdasari/AI-Email-Reply-Generator/
```

Navigate into the project folder:

```id="5vyqbn"
cd AI-Email-Reply-Generator
```

Install the required Python packages:

```id="37awjv"
pip install -r requirements.txt
```

---

## API Key Setup

This application requires a Google Gemini API key.

1. Visit Google AI Studio:

   https://aistudio.google.com

2. Generate an API key.

3. Create a `.env` file in the project directory.

4. Add your API key:

```id="a7ifm9"
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is ignored by Git to prevent exposing sensitive information.

---

## Running the Application

Start the Streamlit application with the following command:

```id="1ppw31"
python -m streamlit run app.py
```

After running the command, the application will open in your browser.

---

## Example Usage

Example input email:

```id="qga4zn"
Hello, I would like to know the pricing details for your product.
```

Generated AI response:

```id="irh7ne"
Thank you for your interest in our product. Our pricing plans start from $29 per month. Please let us know if you would like additional details or a demonstration.
```

---

## Author

Praneeth Dasari

---