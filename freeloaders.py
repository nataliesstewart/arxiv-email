from emailgen import *
import os
from dotenv import load_dotenv
load_dotenv(".env")



USER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")
FREELOADERS = os.environ.get("FREELOADERS")

# FREELOADERS variable should be structured like:

# example1@gmail.com:math.AT,math.AG
# example2@gmail.com:math.NT



list_of_recipients = FREELOADERS.split('\n')

for x in list_of_recipients:
	recipient = x.split(':')[0]
	subjs = x.split(':')[1]

	subjprefs = subjs.split(',')
	send_email(recipient,subjprefs,USER,PASSWORD)