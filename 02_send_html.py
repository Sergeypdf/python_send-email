import smtplib
import os
from email.mime.text import MIMEText


def send_email():
    sender = "your_email"
    # your password = "your password"
    password = os.getenv("EMAIL_PASSWORD")
    #To send email from any email service, you will need to adjust the SMTP server settings, 
    # including the hostname and port, as well as the security settings (e.g., TLS or SSL).
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open("email_template.html") as file:
            template = file.read()
    except IOError:
        return "The template file doesn't found!"

    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = sender
        msg["Subject"] = "Hyvää syntymäpäivää! Vain tänään, saat jopa 90% alennuksen käyttämällä tarjouskoodia!"
        server.sendmail(sender, sender, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    print(send_email())


if __name__ == "__main__":
    main()
