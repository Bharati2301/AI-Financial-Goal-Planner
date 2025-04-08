import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

def generate_savings_plan(user_input, strategies):
    strategies_text = "\n".join([doc.page_content for doc in strategies])

    prompt = f"""
User Info:
- Monthly Income: ${user_input['income']}
- Monthly Expenses: ${user_input['expenses']}
- Goal: {user_input['goal']}
- Timeline: {user_input['timeline']} months

Relevant Strategies:
{strategies_text}

Please generate a personalized, step-by-step savings plan using the strategies above.
"""

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    try:
        return response.json()[0]['generated_text']
    except Exception as e:
        return f"⚠️ Error generating plan:\n{response.text}"
