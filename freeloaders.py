from emailgen import *
import os
from dotenv import load_dotenv
load_dotenv(".env")



USER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")

FRELOADERS = os.environ.get("FREELOADERS")


# tbraz56@gmail.com,math.AT,math.AG
# tbraz56+1@gmail.com,math.NT


print('freeloaders var is ' + str(FRELOADERS))

list_of_recipients = FRELOADERS.split('\n')
print(' list of recipients is ' + str(list_of_recipients))



