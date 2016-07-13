#!/usr/bin/env python3

import smtplib, json, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


FROM_ADDR = os.environ.get('FROM_ADDR')
MY_PASSWORD = os.environ.get('MY_PASSWORD')
MY_NAME = os.environ.get('MY_NAME')
SMTP_SERVER_NAME = os.environ.get('SMTP_SERVER_NAME')
SMTP_PORT = os.environ.get('SMTP_PORT')
DEFAULT_SUBJECT = "A friendly hello from {}".format(MY_NAME)
DEFAULT_TXT_MSG = """\
Hey {}!\n\nLong time no hear. How are you? I just wanted to say hello and see how you are doing. I hope all is well with you.\n\nSincerely,\n{}
"""
DEFAULT_HTML_MSG = """\
<html>
  <head></head>
  <body>
    <p>Hey {}!</p>
    <p>Long time no hear. How are you? I just wanted to say hello and see how you are doing. I hope all is well with you.</p>
    <p>Sincerely,<br/>{}</p>
  </body>
</html>
"""

def main():
    contacts_name = str(input("What's the contacts first name you want to send an email to? ")).strip() 
    contact = get_contact_object(contacts_name)
    contacts_addr = contact['email']
    contacts_fname = contact['fname']
    msg = MIMEMultipart('alternative')
    msg['From'] = FROM_ADDR
    msg['To'] = contacts_addr
    msg['Subject'] = get_msg_subject()
    body_html, body_txt = get_msg_body(contacts_fname)
    msg.attach(MIMEText(body_txt, 'plain'))
    msg.attach(MIMEText(body_html, 'html'))
    server = smtplib.SMTP(SMTP_SERVER_NAME, SMTP_PORT)
    server.starttls()
    server.login(FROM_ADDR, MY_PASSWORD)
    text = msg.as_string()
    server.sendmail(FROM_ADDR, contacts_addr, text)
    server.quit()

def get_contact_object(first_name):
    """Return contact obj based on given 'FIRST_NAME' arg"""
    json_objects = get_json_objects()
    try:
        for contact_obj in json_objects['contacts']:
            if contact_obj['fname'] == first_name:
                return contact_obj
    except LookupError:
        print("contact not found. Check spelling of contact's first name or make sure the contact exists in the JSON file")
    except Exception as e:
        print('Error: {}'.format(e))


def get_json_objects():
    """Return contact objects from JSON"""
    try:
        with open('contacts.json', 'r') as f:
            return json.loads(f.read())
    except IOError:
        print("File could not be found")
    except Exception as e:
        print("Error: {}".format(e))

def get_msg_subject():
    """Get and return msg subject if it's not empty, 
    otherwise set the msg subject to the default"""
    msg = str(input("What's the subject of this email? If you want the default leave empty and press <ENTER> ")).strip()
    if msg:
        return msg
    else:
        return DEFAULT_SUBJECT

def get_msg_body(contacts_name):
    """Get and return msg body as a tuple if it's not empty, 
    otherwise set the msg body to the default"""
    body = str(input("What's the email message? If you want the default leave empty and press <ENTER> ")).strip()
    html = "<html><body><p>{}</p></body></html>".format(body)
    if body:
        return (html, body)
    else:
        return (DEFAULT_HTML_MSG.format(contacts_name, MY_NAME),
                DEFAULT_TXT_MSG.format(contacts_name, MY_NAME))


if __name__ == '__main__':
    main()
