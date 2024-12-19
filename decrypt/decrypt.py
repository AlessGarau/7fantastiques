from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os


def decrypt_file(key_path: str, file_path: str, decrypt_path: str):
    with open(key_path, "rb") as key:
        cle = key.read()

    if len(cle) not in [16, 24, 32]:
        raise ValueError("La clé doit être de 16, 24 ou 32 octets pour AES.")

    with open(file_path, "rb") as fichier_donnees:
        contenu = fichier_donnees.read()

    iv = contenu[:16]
    donnees_chiffrees = contenu[16:]

    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv))
    decryptor = cipher.decryptor()

    donnees_dechiffrees = decryptor.update(
        donnees_chiffrees) + decryptor.finalize()

    padding_length = donnees_dechiffrees[-1]
    donnees_dechiffrees = donnees_dechiffrees[:-padding_length]

    with open(decrypt_path, "wb") as fichier_sortie:
        fichier_sortie.write(donnees_dechiffrees)

    print(
        f"Les données ont été déchiffrées et enregistrées dans {decrypt_path}")


CHEMIN_CLE = "cle_aes.key"
CHEMIN_DONNEES = "test_chiffre.bin"
CHEMIN_DONNEES_DECHIFFREES = "donnees_dechiffrees.txt"


decrypt_file(CHEMIN_CLE, CHEMIN_DONNEES, CHEMIN_DONNEES_DECHIFFREES)
