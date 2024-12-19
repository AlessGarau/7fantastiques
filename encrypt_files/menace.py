import tkinter as tk

def show_ransom_demand():
    """
    Affiche une fenêtre contenant une demande de rançon fictive,
    incluant des instructions de paiement en Solana.
    """
    # Crée la fenêtre principale
    root = tk.Tk()
    root.title("Demande de Rançon")

    # Message de rançon avec les informations fictives pour Solana
    ransom_note = """
    ATTENTION ! Vos fichiers ont été chiffrés !

    Pour obtenir la clé de déchiffrement, vous devez payer 
    une rançon en Solana.

    Montant : 10 SOL
    Adresse Solana : 5b19wdQkZbqA5yV6BbVox3Ldp5TdrdheSu5w1phx2y5L

    Instructions de paiement :
    - Ouvrez votre portefeuille Solana.
    - Envoyez 10 SOL à l'adresse ci-dessus.
    - Une fois le paiement effectué, contactez-nous à l'adresse email suivante : ransom@fake.com

    Une fois le paiement confirmé, vous recevrez votre clé de déchiffrement.
    """

    # Crée une étiquette (label) avec le message
    label = tk.Label(root, text=ransom_note, font=("Helvetica", 12), padx=20, pady=20)
    label.pack()

    # Crée un bouton pour fermer la fenêtre
    close_button = tk.Button(root, text="Fermer", command=root.quit, font=("Helvetica", 12))
    close_button.pack(pady=10)

    # Affiche la fenêtre
    root.mainloop()

# Appel de la fonction pour afficher la demande de rançon
if __name__ == '__main__':
    show_ransom_demand()

