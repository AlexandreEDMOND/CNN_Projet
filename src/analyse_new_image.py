from keras.preprocessing import image
from keras.models import load_model
import numpy as np
from src.ajout_padding_image import ajout_marges_photo

def predict_image_class(image_path, model_path, taille_photo):
    # Charger le modèle Keras
    model = load_model(model_path)

    # Charger et prétraiter l'image
    img = ajout_marges_photo(image_path)
    img = img.resize(taille_photo)

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Normaliser l'image
    img_array /= 255.0

    # Faire la prédiction
    prediction = model.predict(img_array)

    # Afficher la prédiction
    print("Prédiction :", prediction)

    # Interpréter la prédiction
    if prediction[0][0] > 0.5:  # Vous devrez ajuster cela en fonction de votre modèle
        print("Classe : Classe positive")
    else:
        print("Classe : Classe négative")

