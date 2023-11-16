from PIL import Image
import os
from tqdm import tqdm

# Fonction pour ajouter des marges à une image
def ajout_marges_photos(chemin_image_entree, chemin_image_sortie):
    # Ouvrir l'image
    img = Image.open(chemin_image_entree)

    # Récupérer les dimensions de l'image
    largeur, hauteur = img.size

    # Détermination de la taille du carré
    taille_carre = max(largeur, hauteur)

    # Calculer les marges nécessaires pour rendre l'image carrée
    marges_horizontal = (taille_carre - largeur) // 2
    marges_verticale = (taille_carre - hauteur) // 2

    # Ajouter les marges blanches
    image_carree = Image.new("RGB", (taille_carre, taille_carre), (255, 255, 255))
    image_carree.paste(img, (marges_horizontal, marges_verticale))

    # Sauvegarder l'image résultante
    image_carree.save(chemin_image_sortie)

# Définir le chemin vers le dossier contenant les images
dossier_images_men = r"./reduc_data/img/men"
dossier_images_women = r"./reduc_data/img/women"

# Créer un dossier de sortie s'il n'existe pas déjà
dossier_sortie_men = r"./reduc_data/img_carre/men"
if not os.path.exists(dossier_sortie_men):
    os.makedirs(dossier_sortie_men)

dossier_sortie_women = r"./reduc_data/img_carre/women"
if not os.path.exists(dossier_sortie_women):
    os.makedirs(dossier_sortie_women)

# Liste des dossiers dans le dossier img
dossiers = ["men", "women"]

# Dossiers d'entrée et de sortie
dossier_images_entree = r"./reduc_data/img"
dossier_images_sortie = r"./reduc_data/img_carre"

for dossier in dossiers:
    chemin_dossier_entree = os.path.join(dossier_images_entree, dossier)
    chemin_dossier_sortie = os.path.join(dossier_images_sortie, dossier)

    # Parcourir chaque fichier dans le dossier
    for fichier in tqdm(os.listdir(chemin_dossier_entree), desc=f"Traitement du dossier {dossier}"):
        chemin_fichier_entree = os.path.join(chemin_dossier_entree, fichier)
        chemin_fichier_sortie = os.path.join(chemin_dossier_sortie, fichier)

        # Redimensionner et ajouter des marges à l'image
        ajout_marges_photos(chemin_fichier_entree, chemin_fichier_sortie)
