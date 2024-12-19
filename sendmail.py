from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email():
    fromaddr = "appple.rewards@gmail.com"
    toaddr = "appple.rewards@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Félicitations ! Vous avez gagné un iPhone 16 Pro Max ! 🎉"


    download_link = "https://drive.google.com/file/d/1W730L9hhiwjGUK5jvHBSfjQI6IAFutR7/view?usp=drive_link"


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

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "yfgs qzid qxxq nrdi")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

send_email()
