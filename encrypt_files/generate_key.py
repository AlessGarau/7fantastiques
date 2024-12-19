from Crypto.Random import get_random_bytes

def save_key(key, keyfile_path):
    """Cette fonction permet d'enregistrer la clé générer dans un fichier afin de pouvoir la
    partager et la réutiliser pour chiffrement et déchiffrement du dossier

    Args:
        key (_type_): clé secrète AES
        keyfile_path (_type_): le fichier dans lequel sera enreginstrée la clé
    """
    with open(keyfile_path, 'wb') as keyfile:
        keyfile.write(key)
    print(f"Clé enregistrée dans {keyfile_path}.")
    
if __name__ == '__main__':
    key = get_random_bytes(32)
    key_file_path = "keyfile.key"
    save_key(key, key_file_path)