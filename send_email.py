import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ialoni.py@gmail.com"
    password = "sxtioroyhnddfayp"

    reciever = "ialoni.py@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)