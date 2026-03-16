import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")
# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("AI Email Reply Generator")
email = st.text_area("Paste the Email Here")
if st.button("Generate Reply"):
    prompt = f"""
    Read the following email and write a professional reply.
    Email:
    {email}
    Reply:
    """
    response = model.generate_content(prompt)
    st.subheader("Generated Reply")
    st.write(response.text)