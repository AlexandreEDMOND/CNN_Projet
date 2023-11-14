import os
from PIL import Image
import matplotlib.pyplot as plt

# Fonction permettant de récupérer toutes les dimensions des images d'un dossier
def afficher_dimensions_images(dossier_images):
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


dossier_images_men = r"C:\Users\33678\VsCode\CNN Hommes-Femmes\data\men_redim"
dossier_images_women = r"C:\Users\33678\VsCode\CNN Hommes-Femmes\data\women"

dimensions_images_men = afficher_dimensions_images(dossier_images_men)
dimensions_images_women = afficher_dimensions_images(dossier_images_women)

print(dimensions_images_men[0])
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

plt.figure(figsize=(10, 5))
plt.hist(largeurs_men, bins=100, alpha=0.5, label='Largeur')
plt.hist(hauteurs_men, bins=100, alpha=0.5, label='Hauteur')
plt.title('Histogramme des Dimensions des Images')
plt.xlabel('Dimensions')
plt.ylabel("Nombre d'images")
plt.legend()
plt.show()


plt.figure(figsize=(10, 5))
plt.hist(largeurs_women, bins=100, alpha=0.5, label='Largeur')
plt.hist(hauteurs_women, bins=100, alpha=0.5, label='Hauteur')
plt.title('Histogramme des Dimensions des Images')
plt.xlabel('Dimensions')
plt.ylabel("Nombre d'images")
plt.legend()
plt.show()