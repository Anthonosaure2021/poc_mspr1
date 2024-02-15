import os
import shutil

# URL de votre projet GitLab
GIT_REPO_URL = "http://192.168.189.237/root/poc_mspr1.git"

# Répertoire temporaire où cloner le dépôt
TMP_CLONE_DIR = "/tmp/poc_mspr1"

# Répertoire de destination où déplacer les fichiers
DESTINATION_DIR = "/srv/partage/"

def update_project():
    try:
        # Cloner le dépôt Git dans le répertoire temporaire
        os.system(f"git clone {GIT_REPO_URL} {TMP_CLONE_DIR}")

        # Vérifier si le clonage s'est bien déroulé
        if os.path.exists(TMP_CLONE_DIR):
            # Déplacer les fichiers du répertoire temporaire vers le répertoire de destination
            for root, dirs, files in os.walk(TMP_CLONE_DIR):
                for file in files:
                    source_path = os.path.join(root, file)
                    # Ignorer le répertoire .git
                    if '.git' in source_path:
                        continue
                    dest_path = os.path.join(DESTINATION_DIR, os.path.relpath(source_path, TMP_CLONE_DIR))
                    dest_dir = os.path.dirname(dest_path)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    # Utiliser sudo pour copier les fichiers avec les permissions appropriées
                    os.system(f"sudo cp {source_path} {dest_path}")
            
            print("Mise à jour réussie.")
        else:
            print("Échec du clonage du dépôt.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour du projet : {e}")

if __name__ == "__main__":
    update_project()
