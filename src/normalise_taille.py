from PIL import Image
import os
from tqdm import tqdm


def normalise_taille_photo_from_dossier(nom_dossier, taille_reduite):

    # Chemin vers le dossier contenant les images
    dossier_entrée_images = os.path.join(nom_dossier, "img_carre")
    dossier_sortie_images = os.path.join(nom_dossier, "img_norm")

    # Liste des sous-dossiers (men et women)
    sous_dossiers = ["men", "women"]

    # Parcourir chaque sous-dossier
    for sous_dossier in sous_dossiers:
        chemin_sous_dossier = os.path.join(dossier_entrée_images, sous_dossier)

        # Créer un dossier de sortie s'il n'existe pas déjà
        dossier_sortie = os.path.join(dossier_sortie_images, f"{sous_dossier}_carré")
        os.makedirs(dossier_sortie, exist_ok=True)

        # Parcourir chaque fichier dans le sous-dossier
        for fichier in tqdm(os.listdir(chemin_sous_dossier), desc=f"Traitement du dossier {sous_dossier}"):
            chemin_fichier_entree = os.path.join(chemin_sous_dossier, fichier)
            chemin_fichier_sortie = os.path.join(dossier_sortie, fichier)

            # Ouvrir l'image
            img = Image.open(chemin_fichier_entree)

            # Redimensionner l'image
            img_reduite = img.resize(taille_reduite)

            # Sauvegarder l'image réduite
            img_reduite.save(chemin_fichier_sortie)

    print("Traitement terminé.")
