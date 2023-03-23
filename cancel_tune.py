import requests

with open('openaiapikey.txt', 'r') as infile:
    openai_api_key = infile.read().strip()

fine_tune_id = 'ft-uU7e6V8aSNH4KevAWLK9fwIA'
url = f'https://api.openai.com/v1/fine-tunes/{fine_tune_id}/cancel'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {openai_api_key}'}
response = requests.post(url, headers=headers)
print(response.json())