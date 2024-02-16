import shutil
import requests
from fastapi import FastAPI, UploadFile

API_URL = "https://api-inference.huggingface.co/models/louisebld/pizza-or-not-pizza-model"
token = "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"
headers = {"Authorization": f"Bearer {token}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

app = FastAPI()

@app.get("/my-first-api")
def hello():
    return {"Hello world!"}

@app.post("/predict")
async def predict(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        with open("temp.png", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        output = query("temp.png")
        return output


