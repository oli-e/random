import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP(email, 587)
    server.starttls()
    server.login(email, password)
