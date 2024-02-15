from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "louisebld/pizza-or-not-pizza-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Enregistrez le modèle dans un format compatible avec TorchServe
model.save_pretrained("model")
tokenizer.save_pretrained("model")

