import smtplib
import ssl

#it is a email library  which crestes email client sessions

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "umeshroutgol@gmail.com"
    password = "ycjdvxfkadyizast"
    receiver = "umeshroutgol@gmail.com"
    context = ssl.create_default_context()


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email("message")