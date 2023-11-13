import requests
from key import KEY, GOOGLE
import base64
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def get_apod():
    '''
    get astronomic picture of the day using APOD API
    :return: picture url
    '''
    res = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={KEY}')
    print(res.status_code)
    apod_url = str(res.json()['url'])
    return apod_url


url = get_apod()

def make_pictures_list(directory_name):
    '''
    create dictionary of base64 encoded pixtures
    :param directory_name: Name of picture directory
    :return: Dictionary where keys = file name and values = base64 string
    '''
    icons_list_self = {}
    directory = directory_name
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.png'):
            with open(f, 'rb') as fp:
                binary_fc = fp.read()
                fp.close()
                base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')

            ext = f.split('.')[-1]
            name = f.split('/')[-1][:-4]
            dataurl = f'data:image/{ext};base64,{base64_utf8_str}'
            icons_list_self[name] = dataurl
    return icons_list_self

icons_list = make_pictures_list('assets/images/icon/')

#template email
html1 = '<!doctype html> <html lang="en">  <head> <meta http-equiv="content-type" content="text/html; charset=utf-8"> <meta http-equiv="x-ua-compatible" content="ie=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="icon" href="assets/images/favicon.png" type="image/x-icon"> <link rel="shortcut icon" href="assets/images/favicon.png" type="image/x-icon"> <title>rica | email template </title> <link href="https://fonts.googleapis.com/css?family=nunito:300,300i,400,400i,600,600i,700,700i,800,800i,900,900i&display=swap" rel="stylesheet"> <style type="text/css"> body {{ font-family: nunito, sans-serif; position: relative; background: white; font-size: 14px; color: black; }}  ul {{ margin: 0; padding: 0; }}  li {{ display: inline-block; text-decoration: unset; }}  a {{ text-decoration: none; }}  .btn {{ background-color: #292929; border-color: transparent; -webkit-print-color-adjust: exact; letter-spacing: 0.4px; border-radius: 4px; font-weight: 800; font-size: 14px; line-height: 19px; color: #ffffff; cursor: pointer; padding: 7px 13px; -webkit-box-shadow: 1px 11px 20px 0px rgba(233, 179, 14, 0.12); box-shadow: 1px 11px 20px 0px rgba(233, 179, 14, 0.12); text-transform: capitalize;  }}  .btn:focus {{ outline: none; }}  .text-center {{ text-align: center }}  .template-width {{ width: 724px; }}  .home-section {{ height: 350px; width: 100%; position: relative; }}  .tour-section .tour-img {{ width: 280px; height: auto; margin-top: 20px; }}  .bottom-bg {{ width: 100%; height: 150px; background-blend-mode: overlay; background-repeat: no-repeat; background-size: cover; background-color: rgba(0, 0, 0, 0.16); }}  .choose-section {{ width: 130px; }}  .choose-section img {{ width: 55px; opacity: 0.7; }}  @media (max-width: 767px) {{ .template-width {{ width: 550px; }}  .tour-section .tour-img {{ width: 220px; }}  .choose-section img {{ width: 50px; }}  }}  @media (max-width: 576px) {{ .template-width {{ width: 420px; }}  .header {{ display: block; }}  .header td {{ display: block; text-align: center; }}  .top-bar table {{ margin: 0 auto; float: unset !important; }}  .top-bar table+table {{ margin-top: 10px; }}  .home-section {{ height: 250px; }}  .tour-section .tour-img {{ width: 100%; }}  .choose-section {{ width: 70px; }}  .choose-section img {{ width: 36px; }} }}   @media (max-width: 480px) {{ .template-width {{ width: 300px; }} }} </style> </head>  <body style="margin: 80px auto;"> <table class="template-width" align="center" border="0" cellpadding="0" cellspacing="0" style="background: #fff;  box-shadow: 0px 0px 14px -4px rgba(0, 0, 0, 0.2705882353);"> <tbody> <tr> <td class="top-bar" style="background-color: #3e3e3e; padding: 10px;"> <table style="float: left;" cellpadding="0" cellspacing="0"> <tbody> <tr> <td> <a href="#" style="color: white; padding-right: 15px"> <img src="{phone}" style=" width: 12px; margin-right: 3px;margin-bottom: -1px;"> 123 456 789</a> </td> <td> <a href="#" style="color: white;"> <img src="{maile}" style=" width: 15px; margin-right: 3px; margin-bottom: -3px; "> infor@rica.com</a> </td> </tr> </tbody> </table> <table style="float: right;" cellpadding="0" cellspacing="0"> <tbody> <tr> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="{facebook}" style=" width: 12px;"></a> </td> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="{twitter}" style=" width: 12px;"></a> </td> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="{insta}" style=" width: 12px;"></a> </td> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="{google}" style=" width: 15px;"></a> </td> </tr> </tbody> </table> </td> </tr> <tr> <td> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%"> <tbody> <tr class="home-section" style="background-image: url({urs}); background-position: center; background-size: cover; background-blend-mode: overlay;background-color: rgba(0, 0, 0, 0.14);"> <td> <h5 style="text-align: center; color: white; font-size:calc(26px + (35 - 26) * ((100vw - 320px) / (1920 - 320))); margin: 0; text-transform: capitalize;"> picture of a day!</h5> </td> </tr> <tr> <td> <img src="{effect}" style="width: 100%; margin-top: -60px;"> </td> </tr> </tbody> </table> </td> </tr> <tr> <td style="background-color: #f7f7f7; padding: 10px; text-align: center;"> <a href="#" style="color: black;"> copyright 2023 by erunda</a> </td> </tr> </tbody> </table> </body>  </html>'.format(
    urs=url, facebook=icons_list['facebook'], effect=icons_list['effect'], google=icons_list['google-plus'],
    insta=icons_list['instagram-sketched'], maile=icons_list['mail'], phone=icons_list['phone'],
    twitter=icons_list['twitter'])

def send_email(email_from, passw, email_to, html, smtp_server, port, subject, text):
    '''
    create MIME object and send an email
    :param email_from: email address from which we will send email
    :param passw: password of email
    :param email_to: email where we will send an email
    :param html: html body of email
    :param smtp_server: SMTP server
    :param port: PORT
    :param subject: Subject of email
    :param text: Text
    :return: None
    '''
    msg = MIMEMultipart()
    password = passw
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    text = text
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    #server
    server_str = smtp_server +': '+ port
    server = smtplib.SMTP(server_str)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % msg['To'])


send_email("sevwrestler@gmail.com", GOOGLE, "erunda116@yahoo.com", html1, "smtp.gmail.com", "587", "TEST ! Get your astronomy picture of a day", "Hi Bobrina!")
