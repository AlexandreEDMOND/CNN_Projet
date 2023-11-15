from PIL import Image
import os
from tqdm import tqdm


# Définir le chemin vers le dossier contenant les images
dossier_images_men = r"C:\Users\33678\VsCode\CNN Hommes-Femmes\reduc_data\img\men"
dossier_images_women = r"C:\Users\33678\VsCode\CNN Hommes-Femmes\reduc_data\img\women"

# Créer un dossier de sortie s'il n'existe pas déjà
dossier_sortie_men = r"C:\Users\33678\VsCode\CNN Hommes-Femmes\reduc_data\img_redim\men_redim"
if not os.path.exists(dossier_sortie_men):
    os.makedirs(dossier_sortie_men)

dossier_sortie_women = r"C:\Users\33678\VsCode\CNN Hommes-Femmes\reduc_data\img_redim\women_redim"
if not os.path.exists(dossier_sortie_women):
    os.makedirs(dossier_sortie_women)

largeurs = []
hauteurs = []

# Parcourir toutes les images dans le dossier
for nom_fichier in os.listdir(dossier_images_men):
    chemin_image = os.path.join(dossier_images_men, nom_fichier)

    # Ouvrir l'image avec PIL
    image = Image.open(chemin_image)

    # Obtenir les dimensions d'origine
    largeur, hauteur = image.size

    largeurs.append(largeur)
    hauteurs.append(hauteur)

# Parcourir toutes les images dans le dossier
for nom_fichier in os.listdir(dossier_images_women):
    chemin_image = os.path.join(dossier_images_women, nom_fichier)

    # Ouvrir l'image avec PIL
    image = Image.open(chemin_image)

    # Obtenir les dimensions d'origine
    largeur, hauteur = image.size

    largeurs.append(largeur)
    hauteurs.append(hauteur)

# Calculer la moyenne des rapports
largeur_moyen = sum(largeurs) / len(largeurs)
hauteur_moyen = sum(hauteurs) / len(hauteurs)

# Parcourir toutes les images dans le dossier
for nom_fichier in tqdm(os.listdir(dossier_images_men)):
    chemin_image = os.path.join(dossier_images_men, nom_fichier)

    # Ouvrir l'image avec PIL
    image = Image.open(chemin_image)

    image_redim = image.resize((int(largeur_moyen), int(hauteur_moyen)))

    # Sauvegarder l'image avec des marges dans le dossier de sortie
    chemin_image_marges = os.path.join(dossier_sortie_men, "with_margins_" + nom_fichier)
    image_redim.save(chemin_image_marges)

# Parcourir toutes les images dans le dossier
for nom_fichier in tqdm(os.listdir(dossier_images_women)):
    chemin_image = os.path.join(dossier_images_women, nom_fichier)

    # Ouvrir l'image avec PIL
    image = Image.open(chemin_image)

    image_redim = image.resize((int(largeur_moyen), int(hauteur_moyen)))

    # Sauvegarder l'image avec des marges dans le dossier de sortie
    chemin_image_marges = os.path.join(dossier_sortie_women, "with_margins_" + nom_fichier)
    image_redim.save(chemin_image_marges)