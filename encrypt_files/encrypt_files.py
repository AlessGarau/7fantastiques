import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from generate_key import generate_key

def get_desktop_folder():
    """Détermine le chemin du bureau en fonction du système d'exploitation."""
    if os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:
        return os.path.join(os.environ['HOME'], 'Desktop')

def load_key(keyfile_path):
    with open(keyfile_path, 'rb') as keyfile:
        return keyfile.read()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(file_data, AES.block_size))
    return ciphertext

def secure_delete(file_path):
    try:
        with open(file_path, 'r+b') as f:
            file_size = os.path.getsize(file_path)
            f.write(os.urandom(file_size))
        os.remove(file_path)
    except Exception as e:
        print(f"Erreur lors de la suppression sécurisée de {file_path}: {e}")

if __name__ == '__main__':
    project_dir = os.path.dirname(os.path.abspath(__file__))
    keyfile_path = os.path.join(project_dir, "keyfile.key")
    try:
        key = load_key(keyfile_path)
    except Exception as e:
        generate_key()
        key = load_key(keyfile_path)

    desktop_path = get_desktop_folder()
    folder_path = os.path.join(desktop_path, "dossier_confidentiel")
    encrypted_files = {}
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
                    # ciphertext = encrypt_file(file_path, key)
                    # encrypted_file_path = file_path + ".enc"
                    # with open(encrypted_file_path, 'wb') as f:
                    #     f.write(ciphertext)
                    # encrypted_files[file_path] = encrypted_file_path
                    # secure_delete(file_path)