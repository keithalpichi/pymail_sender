#PyMail Sender

A Python script to send emails through the comfort of the command line

---

## Author:
- [Keith Alpichi](https://keithalpichi.github.io)
- [@keithalpichi](https://twitter.com/keithalpichi)

## Key notes:
- Written in Python3 and utilizes Python's built-in `smtplib` and email modules
- Program reads contact's information from a JSON file (`contacts.json`).
- Extend `contacts.json` with more information than just the contact's email and name. You could possible implement phone numbers and addresses
- Ability to customize the subject and body of email or keep the default you set.

## How to use PyMail Sender
- Make sure you have Git and clone this repo by using `git clone https://github.com/keithalpichi/pymail_sender.git`
- In `email_script.py` set the following in the file directly or as environment variables (like so `export VARIABLE_NAME='value_here'`):
 - `FROM_ADDR`- to the address you are sending from
 - `MY_PASSWORD`- to your email password. This should correspond to `FROM_ADDR`
 - `SMTP_SERVER_NAME`- to the smtp server name. If you're using Google set this to `smtp.gmail.com`. **Note- You must set [Gmail's 'access for less secure apps'](https://support.google.com/accounts/answer/6010255?hl=en) to ON in order for this to work. **
 - `SMTP_PORT`- to the smtp port number. If Google, set to 587 to 465.
 - `DEFAULT_SUBJECT`- to what ever you like or keep the default one provided
 - `DEFAULT_TXT_MSG`- to what ever you like or keep the default one provided
 - `DEFAULT_HTML_MSG`- to what ever you like or keep the default one provided
- Edit `contacts.json` with the appropriate information of each contact. Add in new key-value pairs if you'd like
- Send an email like so `python3 email_script.py` and follow the commands.

# To-do:
- Implement recurring emails on time intervals (days, weeks, months)
- Implement ability to send to more than one contact at a time.
- Implement file attachment
