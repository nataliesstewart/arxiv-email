from emailgen import *
import os
from dotenv import load_dotenv
load_dotenv(".env")



USER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")

def subs_to_list(subs):
	return subs.split(',')


LPEMAIL = os.environ.get("LPEMAIL")
LPSUBS = os.environ.get("LPSUBS")
send_email(LPEMAIL,subs_to_list(LPSUBS),USER,PASSWORD)

MPEMAIL = os.environ.get("MPEMAIL")
MPSUBS = os.environ.get("MPSUBS")
send_email(MPEMAIL,subs_to_list(MPSUBS),USER,PASSWORD)

