import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import os
import time
import csv
from datetime import datetime

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASS = os.getenv('SMTP_PASS')
RECIPIENT = os.getenv('RECIPIENT')
SEND_LIMIT = int(os.getenv('SEND_LIMIT', 100))  # Default 100


def send_email(recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = recipient
    msg['Subject'] = subject

    msg['Date'] = formatdate(localtime=True)

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, recipient, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient}")
        log_email(recipient, subject, 'Sent')
    except Exception as e:
        print(f"Failed to send email: {e}")
        log_email(recipient, subject, 'Failed')


def log_email(recipient, subject, status):
    with open('email_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), recipient, subject, status])


def can_send_email():
    today = datetime.now().date()
    count = 0
    try:
        with open('email_log.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                if timestamp.date() == today:
                    count += 1
        return count < SEND_LIMIT
    except FileNotFoundError:
        return True


def create_email_body(recipient):
    first_part = recipient.split('@')[0]
    body = (f"Dear {first_part},\n\n"
            "This is a test mail for IPSENHO research.\n\n"
            "Kind Regards,\n"
            "Python")
    return body


def send_bulk_emails(recipient, num_emails):
    for i in range(num_emails):
        if can_send_email():
            subject = f"Test Email {i + 1}"
            body = create_email_body(recipient)
            send_email(recipient, subject, body)
            time.sleep(1)
        else:
            print("Daily email limit reached. Try again tomorrow.")
            break


if __name__ == '__main__':
    if RECIPIENT is None:
        print("Please set the RECIPIENT environment variable.")
    else:
        send_bulk_emails(RECIPIENT, SEND_LIMIT)
