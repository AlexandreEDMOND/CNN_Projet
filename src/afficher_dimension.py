import os
from PIL import Image
import matplotlib.pyplot as plt

# Fonction qui renvoie une liste des dimensions des images de dossier_images
def get_dimensions_images(dossier_images):

    dimensions = []
    
    # Parcourir toutes les images dans le dossier
    for nom_fichier in os.listdir(dossier_images):

        chemin_image = os.path.join(dossier_images, nom_fichier)

        # Ouvrir l'image avec PIL
        image = Image.open(chemin_image)

        # Obtenir les dimensions de l'image
        largeur, hauteur = image.size

        dimensions.append((largeur, hauteur))

    return dimensions

# Fonction qui renvoie une liste des rapports () des images de dossier_images
def get_rapport_images(dossier_images):
    rapports = []

    # Parcourir toutes les images dans le dossier
    for nom_fichier in os.listdir(dossier_images):

        chemin_image = os.path.join(dossier_images, nom_fichier)

        # Ouvrir l'image avec PIL
        image = Image.open(chemin_image)

        # Obtenir les dimensions de l'image
        largeur, hauteur = image.size
        rapports.append(largeur/hauteur)

    return rapports

#def afficher_info_images()

dossier_images_reduc_men = r"./reduc_data/img_redim/men"
dossier_images_reduc_women = r"./reduc_data/img_redim/women"

dimensions_images_men = get_dimensions_images(dossier_images_reduc_men)
rapport_men = get_rapport_images(dossier_images_reduc_men)
dimensions_images_women = get_dimensions_images(dossier_images_reduc_women)
rapport_women = get_rapport_images(dossier_images_reduc_women)

# Afficher un histogramme des dimensions
largeurs_men, hauteurs_men = zip(*dimensions_images_men)
plt.figure(figsize=(10, 5))
plt.scatter(largeurs_men, hauteurs_men, marker='o', color='blue', alpha=0.5)

largeurs_women, hauteurs_women = zip(*dimensions_images_women)
plt.scatter(largeurs_women, hauteurs_women, marker='o', color='pink', alpha=0.5)

plt.title('Représentation des Dimensions des Images')
plt.xlabel('Largeur')
plt.ylabel('Hauteur')
plt.show()


# Afficher un histogramme des rapports
plt.plot(rapport_men, marker='o', color='blue', linestyle=' ')
plt.plot(rapport_women, marker='o', color='pink', linestyle=' ')
plt.title('Représentation des Dimensions des Images')
plt.xlabel('Largeur')
plt.ylabel('Hauteur')
plt.show()