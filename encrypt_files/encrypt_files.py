import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from generate_key import save_key

def load_key(keyfile_path):
    with open(keyfile_path, 'rb') as keyfile:
        return keyfile.read()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        file_data = f.read()  # Lire le fichier en mode binaire
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

keyfile_path = "keyfile.key"

if not os.path.exists(keyfile_path):
    key = get_random_bytes(32)
    save_key(key, keyfile_path)
else:
    key = load_key(keyfile_path) 
    
files_to_encrypt = ["dossier_confidentiel/Contrat_de_Prestation.docx", "dossier_confidentiel/Achats_Fournitures.xlsx"]

encrypted_files = {}
for file_path in files_to_encrypt:
    ciphertext = encrypt_file(file_path, key)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)
    encrypted_files[file_path] = encrypted_file_path
    secure_delete(file_path)

