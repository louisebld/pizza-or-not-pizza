# Pizza ?
    Réalisé par Louise Bollard et Tom Thierry - M2 INFO 2024

## Lancement de l'API 🚀

Pour lancer l'API, il suffit de lancer la commande suivante dans le dossier "api":

    pip install fastapi uvicorn python-multipart python-dotenv
    python main.py
    
## Utilisation de l'API 🍕

L'API est accessible à l'adresse suivante : `http://localhost:8000`

Les routes disponibles sont les suivantes :
    /predict : Permet de prédire le type de pizza à partir d'une image

Au lancement de l'API, il faudra attendre quelques secondes pour que le modèle se charge. Ensuite, l'API est prête à être utilisée.

Pour l'API, il faut créer le .env et mettre un token huggingface.

## Lancement du front 🚀

Pour lancer le front-end, il suffit de lancer la commande suivante dans le dossier "front-pizza-or-not-pizza" :

    npm install
    npm run dev

