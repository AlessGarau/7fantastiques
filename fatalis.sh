#!/bin/bash

# Définir le répertoire du projet
PROJECT_DIR="encrypt_files"
MAIN_SCRIPT="encrypt_files.py"
KEY_FILE="keyfile.key"
ADDITIONAL_SCRIPT="generate_key.py"
OUTPUT_NAME="encrypt_files"
TOP_PROJECT_DIR="." # Répertoire du projet (niveau supérieur)

# Vérifier si PyInstaller est installé
if ! command -v pyinstaller &>/dev/null; then
  echo "PyInstaller n'est pas installé. Installation en cours..."
  pip install pyinstaller || {
    echo "Échec de l'installation de PyInstaller. Arrêt du script."
    exit 1
  }
else
  echo "PyInstaller est installé."
fi

# Vérifier si pycryptodome est installé
if ! python -c "import Crypto" &>/dev/null; then
  echo "pycryptodome n'est pas installé. Installation en cours..."
  pip install pycryptodome || {
    echo "Échec de l'installation de pycryptodome. Arrêt du script."
    exit 1
  }
else
  echo "pycryptodome est installé."
fi

# Vérifier si le répertoire du projet existe
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Le répertoire du projet '$PROJECT_DIR' est introuvable. Arrêt du script."
  exit 1
else
  echo "Le répertoire du projet '$PROJECT_DIR' est trouvé."
fi

# Naviguer dans le répertoire du projet
cd "$PROJECT_DIR" || {
  echo "Impossible d'accéder au répertoire du projet. Arrêt du script."
  exit 1
}

# Vérifier si le script principal existe
if [ ! -f "$MAIN_SCRIPT" ]; then
  echo "Le script principal '$MAIN_SCRIPT' est introuvable dans '$PROJECT_DIR'. Arrêt du script."
  exit 1
else
  echo "Le script principal '$MAIN_SCRIPT' est trouvé dans '$PROJECT_DIR'."
fi

# Vérifier si le fichier de clé existe
if [ ! -f "$KEY_FILE" ]; then
  echo "Le fichier de clé '$KEY_FILE' est introuvable dans '$PROJECT_DIR'. Arrêt du script."
  exit 1
else
  echo "Le fichier de clé '$KEY_FILE' est trouvé dans '$PROJECT_DIR'."
fi

# Exécuter PyInstaller pour créer l'exécutable
echo "Création de l'exécutable..."
pyinstaller --onefile \
  --add-data "$KEY_FILE:." \
  --add-data "$ADDITIONAL_SCRIPT:." \
  "$MAIN_SCRIPT" \
  --name "$OUTPUT_NAME" \
  --distpath "../dist" \
  --hidden-import "Crypto" \
  --hidden-import "Crypto.Cipher" \
  --hidden-import "Crypto.PublicKey" \
  --hidden-import "Crypto.Random" \
  --hidden-import "Crypto.Util" \
  --hidden-import "Crypto.Util.Padding" \
  --collect-all "Crypto" || {
  echo "Échec de la création de l'exécutable. Arrêt du script."
  exit 1
}

# Vérifier si la création a réussi
if [ -f "$TOP_PROJECT_DIR/dist/$OUTPUT_NAME" ]; then
  echo "Création réussie. L'exécutable a été généré à '$TOP_PROJECT_DIR/dist/$OUTPUT_NAME'."
else
  echo "Échec de la création. Vérifiez les journaux de PyInstaller pour plus de détails."
  exit 1
fi

# Nettoyer les fichiers temporaires
echo "Nettoyage des fichiers temporaires..."
rm -rf build __pycache__ "$OUTPUT_NAME.spec"

# Message final
echo "Le processus de création de l'exécutable est terminé avec succès !"

read -p "Appuyez sur Entrée pour fermer le terminal..."
