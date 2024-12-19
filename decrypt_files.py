import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from commands.execute import execute
from commands.delete_file import secure_delete

def decrypt_file(file_path: str, key: str):
    with open(file_path, "rb") as file_data:
        ciphertext = file_data.read()

    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)

    decrypted_file_path = file_path.removesuffix('.enc')
    with open(decrypted_file_path, "wb") as file_output:
        file_output.write(plaintext)

    print(f"Les données ont été déchiffrées et enregistrées dans {decrypted_file_path}")
    secure_delete(file_path)

if __name__ == '__main__':
    isDecrypted = execute(decrypt_file)
    if isDecrypted: 
        print('HUGO A DECRYPTÉ')