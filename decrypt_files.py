import os
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad
from commands.execute import execute

def decrypt_file(file_path: str, key: str):
    with open(file_path, "rb") as fichier_donnees:
        contenu = fichier_donnees.read()

    iv = contenu[:16]
    donnees_chiffrees = contenu[16:]

    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv))
    decryptor = cipher.decryptor()

    donnees_dechiffrees = decryptor.update(donnees_chiffrees) + decryptor.finalize()

    padding_length = donnees_dechiffrees[-1]
    donnees_dechiffrees = donnees_dechiffrees[:-padding_length]

    decrypted_file_path = file_path.removesuffix('.enc')
    with open(decrypted_file_path, "wb") as fichier_sortie:
        fichier_sortie.write(donnees_dechiffrees)

    print(f"Les données ont été déchiffrées et enregistrées dans {decrypted_file_path}")

if __name__ == '__main__':
    isDecrypted = execute(decrypt_file)
    if isDecrypted: 
        print('HUGO A DECRYPTÉ')