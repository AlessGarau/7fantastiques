import os
from folder_commands.key.generate_key import generate_key

def load_key(keyfile_path):
    with open(keyfile_path, 'rb') as keyfile:
        return keyfile.read()

def get_key():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    keyfile_path = os.path.join(project_dir, "key", "keyfile.key")
    try:
        return load_key(keyfile_path)
    except Exception as e:
        generate_key()
        return load_key(keyfile_path)

def get_desktop_folder():
    """Détermine le chemin du bureau en fonction du système d'exploitation."""
    if os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:
        return os.path.join(os.environ['HOME'], 'Desktop')

def get_folder_path():
    desktop_path = get_desktop_folder()
    return os.path.join(desktop_path, "dossier_confidentiel")

def execute(func):
    key = get_key()
    folder_path = get_folder_path()
    # encrypted_files = {}
    if not folder_path.endswith("dossier_confidentiel"):
        folder_path = None
        print("Le chemin ne se termine pas par 'dossier_confidentiel'. folder_path est défini sur None pour éviter une grosse bétise dans le cadre de l'évaluation.")
    else :
        if not os.path.exists(folder_path):
            print("Le chemin spécifié n'existe pas.")
        elif not os.path.isdir(folder_path):
            print("Le chemin spécifié n'est pas un dossier.")
        else:
            print("Dossier valide, démarrage de l'exploration...")
            for current_folder, child_folders, files in os.walk(folder_path):
                print(f"Exploration du dossier : {current_folder}")
                for file in files:
                    file_path = os.path.join(current_folder, file)
                    print(f"Fichier trouvé : {file_path}")
                    func(file_path, key)