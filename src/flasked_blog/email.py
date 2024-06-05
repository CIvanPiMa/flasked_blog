import os
from typing import Dict, Tuple, Sequence
import smtplib
from logging import getLogger

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import flasked_blog.constants as c

EMAIL_RESPONSE = Dict[str, Tuple[int, bytes]]

def send_email(subject: str, body: str, to_emails: Sequence[str]) -> None:
    """
    Send an email, using the bot account to my personal email.

    Attributes:
    ===========
    subject: str
        The subject of the email.
    body: str
        The body of the email.
    to_emails: Sequence[str]
        A list of email addresses to send the email to.

    Raises:
    =======
    ValueError: 
        If the environment variables GOOGLE_ACCOUNT_BOT_EMAIL and GOOGLE_ACCOUNT_BOT_PASSWORD are not set.
    """
    try:
        from_email = os.environ[c.GOOGLE_ACCOUNT_BOT_EMAIL_ENV_VAR]
        from_password = os.environ[c.GOOGLE_ACCOUNT_BOT_PASSWORD_ENV_VAR]
    except KeyError as e:
        raise ValueError(f"Make sure the environment variables {c.GOOGLE_ACCOUNT_BOT_EMAIL_ENV_VAR} and {c.GOOGLE_ACCOUNT_BOT_PASSWORD_ENV_VAR} are set. {e}")

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, from_password)
        response: EMAIL_RESPONSE = server.sendmail(from_email, to_emails, msg.as_string())

    if response:
        getLogger(__name__).error(f"Failed to send email. {response}")



def get_personal_email() -> str:
    """
    Get the personal email from the environment variables.

    Returns:
    ========
    str
        The personal email address.
    """
    try:
        return os.environ[c.GOOGLE_ACCOUNT_PERSONAL_EMAIL_ENV_VAR]
    except KeyError as e:
        raise ValueError(f"Make sure the environment variable {c.GOOGLE_ACCOUNT_PERSONAL_EMAIL_ENV_VAR} is set. {e}")


def generate_email_content(form: Dict[str, str]) -> Tuple[str, str]:
    """
    Generate the email content from the form.
    The form should have the keys: "name", "email" and "message".

    Attributes:
    ===========
    form: Dict[str, str]
        The form data.

    Returns:
    ========
    Tuple[str, str]
        The subject and body of the email.
    """
    name = form.get("name", "")
    email = form["email"]
    message = form["message"]
    subject = f"New message from: '{email}'"
    body = f"{name} says:\n{message}" if name else f"Message:\n{message}"
    return subject, body
