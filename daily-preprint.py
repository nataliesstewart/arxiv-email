from generate-email import send_email
import os
from dotenv import load_dotenv


load_dotenv(".env")

USER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")
RECIPIENT = os.environ.get("RECIPIENT")
subscriptions = ["math.AT","math.AG"]


send_email(RECIPIENT,subscriptions,USER,PASSWORD)