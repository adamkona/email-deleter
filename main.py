import imaplib
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # iCloud mail server
    mailbox = imaplib.IMAP4_SSL("imap.mail.me.com", 993)
    mailbox.login(os.environ.get("EMAIL"), os.environ.get("EMAIL_PASSWORD"))
    mailbox.select('Inbox')
    typ, data = mailbox.search(None, '(SINCE "31-Jul-2022" BEFORE "31-Oct-2022")')
    print(f'{len(data[0].split())} emails found')

    # Marks marks emails from search for deletion and deletes them
    # for num in data[0].split():
    #     mailbox.store(num, '+FLAGS', '\\Deleted')
    # mailbox.expunge()
    mailbox.close()
    mailbox.logout()

main()