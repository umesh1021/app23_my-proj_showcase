import smtplib
import ssl

#it is a email library  which crestes email client sessions

host="smtp.gmail.com"
port=465
username="umeshroutgol@gmail.com"
password="ycjdvxfkadyizast"

receiver="ashokroutgol@gmail.com"
context=ssl.create_default_context()

message="""\

Subject=Hi!
How are you ?
Bye!
"""

context=ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)