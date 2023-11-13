import requests
from key import KEY, GOOGLE
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
url = ''
def get_apod():
    res = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={KEY}')
    print(res.status_code)
    print(res.json()['url'])
    global url
    url = res.json()['url']

html1 = r'<!doctype html> <html lang="en">  <head> <meta http-equiv="content-type" content="text/html; charset=utf-8"> <meta http-equiv="x-ua-compatible" content="ie=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="icon" href="assets/images/favicon.png" type="image/x-icon"> <link rel="shortcut icon" href="assets/images/favicon.png" type="image/x-icon"> <title>rica | email template </title> <link href="https://fonts.googleapis.com/css?family=nunito:300,300i,400,400i,600,600i,700,700i,800,800i,900,900i&display=swap" rel="stylesheet"> <style type="text/css"> body {{ font-family: nunito, sans-serif; position: relative; background: white; font-size: 14px; color: black; }}  ul {{ margin: 0; padding: 0; }}  li {{ display: inline-block; text-decoration: unset; }}  a {{ text-decoration: none; }}  .btn {{ background-color: #292929; border-color: transparent; -webkit-print-color-adjust: exact; letter-spacing: 0.4px; border-radius: 4px; font-weight: 800; font-size: 14px; line-height: 19px; color: #ffffff; cursor: pointer; padding: 7px 13px; -webkit-box-shadow: 1px 11px 20px 0px rgba(233, 179, 14, 0.12); box-shadow: 1px 11px 20px 0px rgba(233, 179, 14, 0.12); text-transform: capitalize;  }}  .btn:focus {{ outline: none; }}  .text-center {{ text-align: center }}  .template-width {{ width: 724px; }}  .home-section {{ height: 350px; width: 100%; position: relative; }}  .tour-section .tour-img {{ width: 280px; height: auto; margin-top: 20px; }}  .bottom-bg {{ width: 100%; height: 150px; background-blend-mode: overlay; background-repeat: no-repeat; background-size: cover; background-color: rgba(0, 0, 0, 0.16); }}  .choose-section {{ width: 130px; }}  .choose-section img {{ width: 55px; opacity: 0.7; }}  @media (max-width: 767px) {{ .template-width {{ width: 550px; }}  .tour-section .tour-img {{ width: 220px; }}  .choose-section img {{ width: 50px; }}  }}  @media (max-width: 576px) {{ .template-width {{ width: 420px; }}  .header {{ display: block; }}  .header td {{ display: block; text-align: center; }}  .top-bar table {{ margin: 0 auto; float: unset !important; }}  .top-bar table+table {{ margin-top: 10px; }}  .home-section {{ height: 250px; }}  .tour-section .tour-img {{ width: 100%; }}  .choose-section {{ width: 70px; }}  .choose-section img {{ width: 36px; }} }}   @media (max-width: 480px) {{ .template-width {{ width: 300px; }} }} </style> </head>  <body style="margin: 80px auto;"> <table class="template-width" align="center" border="0" cellpadding="0" cellspacing="0" style="background: #fff;  box-shadow: 0px 0px 14px -4px rgba(0, 0, 0, 0.2705882353);"> <tbody> <tr> <td class="top-bar" style="background-color: #3e3e3e; padding: 10px;"> <table style="float: left;" cellpadding="0" cellspacing="0"> <tbody> <tr> <td> <a href="#" style="color: white; padding-right: 15px"> <img src="assets/images/icon/phone.png" style=" width: 12px; margin-right: 3px;margin-bottom: -1px;"> 123 456 789</a> </td> <td> <a href="#" style="color: white;"> <img src="assets/images/icon/mail.png" style=" width: 15px; margin-right: 3px; margin-bottom: -3px; "> infor@rica.com</a> </td> </tr> </tbody> </table> <table style="float: right;" cellpadding="0" cellspacing="0"> <tbody> <tr> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="assets/images/icon/facebook.png" style=" width: 12px;"></a> </td> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="assets/images/icon/twitter.png" style=" width: 12px;"></a> </td> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="assets/images/icon/instagram-sketched.png" style=" width: 12px;"></a> </td> <td> <a href="#" style="color: white; padding-right: 15px;"> <img src="assets/images/icon/google-plus.png" style=" width: 15px;"></a> </td> </tr> </tbody> </table> </td> </tr> <tr> <td> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%"> <tbody> <tr class="home-section" style="background-image: url({}); background-position: center; background-size: cover; background-blend-mode: overlay;background-color: rgba(0, 0, 0, 0.14);"> <td> <h5 style="text-align: center; color: white; font-size:calc(26px + (35 - 26) * ((100vw - 320px) / (1920 - 320))); margin: 0; text-transform: capitalize;"> picture of a day!</h5> </td> </tr> <tr> <td> <img src="assets/images/effect.png" style="width: 100%; margin-top: -60px;"> </td> </tr> </tbody> </table> </td> </tr> <tr> <td style="background-color: #f7f7f7; padding: 10px; text-align: center;"> <a href="#" style="color: black;"> copyright 2020 rica by pixelstrap</a> </td> </tr> </tbody> </table> </body>  </html>'.format(url)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    get_apod()

    # create message object instance
    msg = MIMEMultipart()
    #message = "Thank you"
    # setup the parameters of the message
    password = GOOGLE
    msg['From'] = "sevwrestler@gmail.com"
    msg['To'] = "irina.gubanova2h@gmail.com"
    msg['Subject'] = "TEST ! Get your astronomy picture of a day"
    # add in the message body
    text = "Hi Bobrina!"
    #html = open('offer.html', 'r').read()
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html1, 'html')
    msg.attach(part1)
    msg.attach(part2)


    #msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % msg['To'])


