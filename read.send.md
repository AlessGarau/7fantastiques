## sendmail.py

La fonction `send_email` permettant d'envoyer un email promotionnel via le protocole serveur SMTP de Gmail.

### Objectifs Fonctionnels

- Envoyer un email à un destinataire unique.

- Fournir un lien cliquable dans l’email pour réclamer le "cadeau".

- Utiliser un serveur SMTP pour assurer la transmission.

### Description de la Fonctionnalité

- **Paramètres** :

- La fonction `send_email` n’accepte pas de paramètres. Elle est entièrement configurée avec des valeurs fixes :

  - Adresse de l’expéditeur.
  - Adresse du destinataire.
  - Sujet de l’email.
  - Contenu HTML de l’email.

- **Ressources**:

Bibliothèque [smtplib](https://docs.python.org/3/library/smtplib.html) : Gère la connexion au serveur SMTP.

Bibliothèque [email.mime](https://docs.python.org/3/library/email.mime.html) : Structure les emails en parties distinctes.


### Explication du Code

**1. Importation des Modules**

```python 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
```

- **MIMEMultipart** : Permet de créer un email avec plusieurs parties (texte, HTML, fichiers attachés, etc.).

- **MIMEText** : Permet d’ajouter une partie texte ou HTML à l’email.

- **smtplib** : Gère l’envoi d’emails via le protocole SMTP.

**2. Initialisation des Paramètres**

```python 
fromaddr = "lmlmlmiranda@gmail.com"
toaddr = "lmlmlmiranda@gmail.com"
```

- **fromaddr** : Adresse email de l’expéditeur.

- **toaddr** : Adresse email du destinataire.

**3. Création de l’Email**

```python 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Félicitations ! Vous avez gagné un iPhone 16 Pro Max ! 🎉"
```
- **msg** : Objet MIMEMultipart représentant l’email.

- **msg['From']** : Champ "expéditeur".

- **msg['To']** : Champ "destinataire".

- **msg['Subject']** : Champ "object".


**4. Contenu HTML**
```python
download_link = "https://drive.google.com/file/d/1RKtJLAj84g2k6XGRAB1tW554tJ6cWW5W/view?usp=drive_link"

body = f"""<html>
<body>
<p>Cher(e) utilisateur(trice),</p>
<p>Félicitations ! Vous avez été sélectionné(e) au hasard pour recevoir le tout nouvel iPhone 16 Pro Max dans le cadre de notre campagne de fidélisation.</p>
<p>Pour réclamer votre cadeau, il vous suffit de :</p>
<a href="{download_link}" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: white; background-color: #D10000; text-align: center; text-decoration: none; border-radius: 5px; font-weight: bold;">Réclamer mon iPhone</a>
<p>⚠️ Attention : Cette offre est valable uniquement pendant 24 heures. Après cela, nous devrons offrir ce téléphone à un autre participant chanceux.</p>
<p>Ne manquez pas cette opportunité unique !</p>
<p>Cordialement,<br>L'équipe Apple Rewards</p>
</body>
</html>"""
```
- **download_link** : URL incluse dans l’email pour réclamer le cadeau.

- **body** : Texte HTML de l’email. Il inclut une mise en page enrichie avec des paragraphes et un bouton.

**5. Ajout du Contenu à l’Email**

```python
msg.attach(MIMEText(body, 'html'))
```

- **MIMEText(body, 'html')** : Crée une partie HTML.

- **msg.attach** : Ajoute la partie HTML à l’email.

**6. Connexion au Serveur SMTP**

```python
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "tirh qrox uphy giiq")
```

- **smtplib.SMTP('smtp.gmail.com', 587)** : Connexion au serveur SMTP de Gmail via le port 587 (TLS).

- **server.starttls()** : Initialise une connexion cryptée.

- **server.login(fromaddr, "mot_de_passe")** : Authentification avec l’adresse email et son mot de passe.

⚠️ Important : Ce mot de passe est un mot de passe d’application spécifique à Gmail. [Comment configurer un mot de passe d'application](https://support.google.com/accounts/answer/185833?visit_id=638699573054161696-3051567020&p=InvalidSecondFactor&rd=1) !

**7. Envoi de l’Email**

```python
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
```

- **msg.as_string()** : Convertit l’objet email en une chaîne prête à être envoyée.

- **server.sendmail(fromaddr, toaddr, text)** : Envoie l’email.

- **server.quit()** : Ferme la connexion avec le serveur SMTP.