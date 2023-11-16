from src.training_CNN import training_CNN
from src.ajout_padding_image import *
from src.normalise_taille import *
from src.analyse_new_image import *
import os


if __name__ == "__main__":

  nom_dossier_data = "./data"
  taille_photo = (300, 300)
  nom_chemin_sauvegarde_modele = "./models/model_from_data_300_300.keras"

  #ajout_marges_photo_from_dossier(nom_dossier_data)

  #normalise_taille_photo_from_dossier(nom_dossier_data, taille_photo)

  #training_CNN(nom_dossier_data, taille_photo, nom_chemin_sauvegarde_modele)

  nom_dossier_test = "./test_image"

  for fichier in os.listdir(nom_dossier_test):
    print(f"\nRésultat de la phote {fichier} :")
    chemin_fichier_entree = os.path.join(nom_dossier_test, fichier)
    predict_image_class(chemin_fichier_entree, nom_chemin_sauvegarde_modele, taille_photo)
