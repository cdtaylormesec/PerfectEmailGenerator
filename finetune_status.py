import os
import requests
import openai
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_fine_tune_status():
    fine_tunes = openai.FineTune.list()
    for fine_tune in fine_tunes['data']:
        print(f"Fine-tune id: {fine_tune['id']}, status: {fine_tune['status']}")

get_fine_tune_status()