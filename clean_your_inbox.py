import imaplib

imap = imaplib.IMAP4_SSL("imap.gmail.com")

email_user = 'votre adresse email'
email_pass = 'le mot de passe d''application évoqué dans ReadMe'
imap.login(email_user, email_pass)

imap.select("inbox")

status, messages = imap.search(None, 'FROM "Grammarly Insights"')
email_ids = messages[0].split()

for email_id in email_ids:
    imap.store(email_id, "+FLAGS", "\\Deleted")

imap.expunge()

imap.close()
imap.logout()
