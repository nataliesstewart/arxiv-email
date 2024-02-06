from emailgen import *
import os
from dotenv import load_dotenv


load_dotenv(".env")



USER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")

FREELOADERS = os.environ.get("FREELOADERS")

for person in FREELOADERS:
	recipient = person[0]
	subscription_prefs = person[1]
	send_email(recipient,subscription_prefs,USER,PASSWORD)
