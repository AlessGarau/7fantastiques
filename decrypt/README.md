1.  Points clés :
    Type : Chiffrement symétrique (même clé pour chiffrer et déchiffrer).
    Bloc : Fonctionne par blocs de 128 bits (16 octets).
    Clé : Peut avoir une longueur de 128, 192 ou 256 bits.
    Sécurité : Considéré comme très sûr et utilisé dans les standards internationaux.

2.  Fonctionnement :
    Chiffrement par blocs :
    Les données sont divisées en blocs de 16 octets.
    Si la taille des données n'est pas un multiple de 16, un padding est ajouté.
    Modes de chiffrement : AES ne travaille qu'avec des blocs fixes

    Vecteur d'initialisation (IV) :
    Un IV unique de 16 octets est souvent utilisé dans des modes comme CBC pour éviter les répétitions.

3.  Avantages :
    Rapide et efficace : Optimisé pour le matériel et les logiciels modernes.
    Sécurisé : Résistant aux attaques cryptographiques connues (si bien implémenté).
    Standardisé : Utilisé dans HTTPS, VPN, Wi-Fi, etc.
    
4.  Exemple d'utilisation :
    Chiffrement d'un fichier : Ajout d'un IV au début du fichier suivi des données chiffrées.
    Déchiffrement : Extraction de l'IV et utilisation de la clé pour récupérer les données originales.

5.  Pourquoi ne pas decrypter directement dans le même fichier ?  
        Préservation des données originales :
            Lorsque tu déchiffres des données, si tu écris directement dans le même fichier, tu risques de perdre les données chiffrées en cas d'erreur dans le processus de déchiffrement. Par exemple, si quelque chose ne va pas pendant le déchiffrement (corruption de fichier, erreur de clé, etc.), tu n'auras plus de copie de secours.
            En créant un fichier de sortie distinct pour les données déchiffrées, tu conserves les données originales sous forme chiffrée, ce qui permet d'éviter la perte de ces données en cas de problème.
        
    Principes de bonne pratique en programmation :
        Séparation des responsabilités :
            Le fichier d'entrée contient les données chiffrées et doit rester inchangé pendant tout le processus de déchiffrement. Le fichier de sortie contient les données déchiffrées.
        Facilité les tests : 
            En déchiffrant vers un fichier différent, tu peux plus facilement tester ton déchiffrement en comparant les données originales et déchiffrées, sans avoir à toucher aux fichiers sources.
