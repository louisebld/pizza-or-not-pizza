from transformers import AutoTokenizer, AutoModelForImageClassification
from PIL import Image
import requests
from io import BytesIO
import torch

# Charger le tokenizer et le modèle
tokenizer = AutoTokenizer.from_pretrained("louisebld/pizza-or-not-pizza-model")
model = AutoModelForImageClassification.from_pretrained("louisebld/pizza-or-not-pizza-model")

# Télécharger ou charger votre image
image_url = "https://cdn2.thecatapi.com/images/ja.jpg"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Prétraiter l'image et obtenir les embeddings
inputs = tokenizer(images=image, return_tensors="pt")
outputs = model(**inputs)

# Obtenir les probabilités de classification
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Afficher les résultats
labels = ['Not Pizza', 'Pizza']
label_id = torch.argmax(probabilities)
print(f"Prediction: {labels[label_id]} - Confidence: {probabilities[0, label_id]:.2%}")
