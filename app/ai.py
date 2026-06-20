import os

from dotenv import load_dotenv
from google import genai

from app.prompts import (
    JOURNAL_ANALYSIS_PROMPT,
    WELLNESS_CHAT_PROMPT,
    EMERGENCY_CHECK_PROMPT
)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY
)

MODEL = "gemini-2.5-flash"


def call_llm(prompt: str):

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


# ====================================
# JOURNAL ANALYSIS
# ====================================

def analyze_journal(journal: str):

    prompt = JOURNAL_ANALYSIS_PROMPT.format(
        journal=journal
    )

    return call_llm(prompt)


# ====================================
# WELLNESS CHAT
# ====================================

def wellness_chat(message: str):

    prompt = WELLNESS_CHAT_PROMPT.format(
        message=message
    )

    return call_llm(prompt)


# ====================================
# EMERGENCY CHECK
# ====================================

def emergency_detection(journal: str):

    prompt = EMERGENCY_CHECK_PROMPT.format(
        journal=journal
    )

    result = call_llm(prompt)

    result = result.lower()

    return "alert=true" in result