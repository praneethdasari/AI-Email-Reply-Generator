# AI Email Reply Generator

AI Email Reply Generator is a simple automation tool that generates professional email responses using Google Gemini AI and Python. The application reads an incoming email and produces an appropriate reply automatically.

This project demonstrates how generative AI can be used to automate customer communication tasks such as responding to product inquiries or support requests.

## Features

* Generates professional email replies automatically
* Understands the intent of the input email
* Simple web interface built with Streamlit
* Uses Google Gemini API for AI text generation

## Technologies Used

* Python
* Streamlit
* Google Generative AI (Gemini)
* python-dotenv

## Project Structure

```
AI-Email-Reply-Generator
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

Note: The `.env` file is used to store the API key and should not be uploaded to GitHub.

## Installation

Clone the repository:

```
git clone https://github.com/praneethdasari/AI-Email-Reply-Generator.git
```

Navigate to the project folder:

```
cd AI-Email-Reply-Generator
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project directory and add your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

You can obtain an API key from Google AI Studio:

https://aistudio.google.com

## Running the Application

Run the Streamlit application with the following command:

```
python -m streamlit run app.py
```

The application will open automatically in your web browser.

## Example

Input email:

```
Hello, I would like to know the pricing for your product.
```

Generated reply:

```
Thank you for your interest in our product. Our pricing plans start from $29 per month. Please let us know if you would like additional information or a product demonstration.
```

## Future Improvements

* Add multiple response styles (professional, friendly, sales)
* Email summarization feature
* Copy generated reply button
* Gmail integration for automated replies

## Author

Praneeth
