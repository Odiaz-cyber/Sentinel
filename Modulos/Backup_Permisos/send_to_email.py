#!/usr/bin/python3
from termcolor import colored
# Enviar correos
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail:

    def send_email(self,subject,body,sender,recipients,password , attachment_path=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ','.join(recipients)
    
        # Cuerpo del mensaje
        msg.attach(MIMEText(body, 'plain'))
    
        # Adjuntar archivo si se proporciona
        if attachment_path:
            with open(attachment_path, 'rb') as f:
                part = MIMEApplication(f.read(), Name=attachment_path)
                part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
                msg.attach(part)
    
        with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp_server:
            smtp_server.login(sender , password)
            smtp_server.sendmail(sender , recipients , msg.as_string())
        print(colored(f"\n[+] Email Enviado\n" , 'green'))
    
