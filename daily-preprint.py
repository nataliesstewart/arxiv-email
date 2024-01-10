# HOW TO RUN IT:
# 1. Open the .env file and input your email and password
#
# 2. Update your subscription preferences here:
subscriptions = ["math.AT","math.AG"]



import csv
import feedparser
from datetime import date
today = date.today()

# Get a list of math subjects and math tags from 'subj-list.csv'
with open('subj-list.csv','r') as f:
    reader = csv.reader(f)
    mathSubjects = list(reader)

all_possible_tags = [x[0] for x in mathSubjects]
all_possible_subjects = [x[1] for x in mathSubjects]

# Generate HTML for the email
html_top = """\
<html>
<head>
	<style>
		html{
			background-color: #F2F3F4;
		}
		p{
			color:#2B303A;
		}
		.colored {
			color: blue;
		}
		#body {
			font-size: 14px;
		}
	  	#banner{
	  		width:100%;
	  		font-size:18px;
	  		color: #F4F2F3;
	  		text-align:center;
	  		padding:1px;
	  		border-radius: 20px;
	  		background-color: #515c5d;
		}

		.banner_table{
			border-radius: 20px;
			text-align: center;
			color: white;
			background-size: cover;
		}

		#banner h1{
			width: 75%;
			display: inline-block;
			margin: 10px;
		}


		#body a{
			color: #0C7C59;
		}
		#subjectTitle{
			width:inherit;
			font-size:14px;
			color : #984447;
			text-align:center;
		}
		#subject{
			text-align:left;
		}

		#tag, #xlistedtag, #updated{
			display: inline;
			color: white;
			border-radius: 8px;
			padding: 1px;
			font-size: 10px;
			margin: 2px;
		}

		#tag{
			background-color: #984447;
		}
		#xlistedtag{
			background-color: #a65094;
		}

		#updated{
			background-color: #575757;
		}


		.container {
		  position: relative;
		  text-align: center;
		  color: yellow;
		}

		.container h1{
		   z-index: 2;
		   position: absolute;
		   top: 50%;
		    left: 50%;
		    right: 50%;
		    font-size: 20px;
		    width: inherit;
		    padding: 0;
		    margin: 0;
		}

		.container img{
		    z-index: 1;
		    width: 100%;
		    height: 100%;
		    position: absolute;
		    top:0;
		    right:0;
		    bottom:0;
		    left:0;
		}


	</style>
</head>
<body>
	<div id="banner">
		<h1>Daily Math Feed: """ + str(today.strftime("%B %d, %Y")) + """</h1>
	</div>

<!--<div class="container">
	<h1>TESTING</h1>
  <img src="cid:image1" alt="math-banner" style="width:inherit;">
  
</div> -->




	<br>
	<div id="body">
"""
text_top = "Daily Math Feed\n\n"

html_bottom = """\
	</div>
</body>
</html>
"""

rss_html = ""
rss_text = ""

for subj in subscriptions:

	# Goes from math.AG -> Algebraic Geometry
	subj_index = all_possible_tags.index(subj)
	subj_title = all_possible_subjects[subj_index]


	rss_url = "http://arxiv.org/rss/" + str(subj)
	Feed = feedparser.parse(rss_url)
	pointer = Feed.entries

	rss_html = rss_html + """\t<div id="subjectTitle">\n\t<h2 id="subjectTitleText">""" + str(subj) + """</h2>\n\t</div>\n\t<div id="subject">\n"""
	text_html = str(subj) + '\n'

	for entry in pointer:

		##
		papertitle = str(entry.title)
		papersplit = papertitle.split('arXiv')
		papersplit[0] = papersplit[0][:-3]
		papersplit[1] = papersplit[1][11:]

		list_of_tags = []


		# Figure out what the associated tag (e.g. "math.AG") is for the given paper
		for x in mathSubjects:
			if x[0] in papersplit[1]:
				list_of_tags.append(x[1])

		# Make HTML for each tag for the paper
		tags_html = ''
		for tag in list_of_tags:
			# Check if the paper was crosslisted by seeing if the tag is the same as the current subject the API is querying
			if tag == subj_title:
				newtag = '<div id="tag">' + str(tag) + '</div>'
			else:
				newtag = '<div id="xlistedtag">' + str(tag) + '</div>'
			
			tags_html = tags_html + newtag
		

		# Make HTML to see the paper version
		version = papersplit[1].split(' ')[0]
		version_html = ''
		if version != 'v1':
			version_html = version_html + '<div id="updated">' + str(version) + ' UPDATED</div>'

		##
		entry_html = '\n\t\t<div id="paper"><b>Title:</b> <a id="paperTitle" href="' + str(entry.id) + '">' + str(papersplit[0]) + '</a>' + tags_html + version_html + '<br>\n\t<b> Authors: </b>' + str(entry.author) + '<br>\n\t\t' + str(entry.summary) + '</div>\n<hr>'
		entry_text = str(entry.title) + '\n\t' + str(entry.author) + '\n\n\t\t' + str(entry.summary)

		rss_html = rss_html + entry_html
		rss_text = rss_text + entry_text


	rss_html = rss_html + "\t</div>\n"


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


import os
from dotenv import load_dotenv


load_dotenv(".env")

USER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")
RECIPIENT = os.environ.get("RECIPIENT")

# me == my email address
# you == recipient's email address
me = USER
you = RECIPIENT


msg = MIMEMultipart('alternative')
msg['Subject'] = "Daily Math Feed: " + str(today.strftime("%B %d, %Y"))
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = text_top + rss_text
html = html_top + rss_html + html_bottom


###
# Uncomment the following for testing:

# testingpage = open('test.html','w')
# testingpage.write(html)




# Record the MIME types of both parts,text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)


fp = open('math-banner-800.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(USER, PASSWORD)
mail.sendmail(me, you, msg.as_string())
mail.quit()



######################################################

# References:
#
# https://dev.to/maxhumber/how-to-send-and-schedule-emails-with-python-dnb
#
# https://stackoverflow.com/a/26369282
#
# 