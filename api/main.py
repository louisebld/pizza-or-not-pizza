import requests

API_URL = "https://api-inference.huggingface.co/models/louisebld/pizza-or-not-pizza-model"
token = "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"
headers = {"Authorization": f"Bearer {token}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("pizza.png")
print(output)