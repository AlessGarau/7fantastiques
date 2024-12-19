import os

def secure_delete(file_path):
    try:
        with open(file_path, 'r+b') as f:
            file_size = os.path.getsize(file_path)
            f.write(os.urandom(file_size))
        os.remove(file_path)
        print(f'Fichier : {file_path} supprimé avec succès')
    except Exception as e:
        print(f"Erreur lors de la suppression sécurisée de {file_path}: {e}")