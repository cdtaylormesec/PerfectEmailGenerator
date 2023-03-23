import openai

with open('openaiapikey.txt', 'r') as infile:
    open_ai_api_key = infile.read()

openai.api_key = open_ai_api_key

def get_fine_tune_status():
    fine_tunes = openai.FineTune.list()
    for fine_tune in fine_tunes['data']:
        print(f"Fine-tune id: {fine_tune['id']}, status: {fine_tune['status']}")

get_fine_tune_status()
