# arxiv-email
 
This sends an automated HTML-formatted email using arXiv's API. Installation instructions are below.


1. Fork this repository
2. Make sure you have your gmail credentials ready to go. It may not work unless you set up a [new app password](https://support.google.com/mail/answer/185833?hl=en-GB) on gmail (if you can't find this, use "Search Google Account").
3. In your forked repository, go to Settings > Secrets and variables > Actions, and add your credentials securely there. Create three Repository Secrets:
* `GMAIL_USER` - this is the email that will send your daily emails
* `GMAIL_PASSWORD` - the app password for that email
* `RECIPIENT` - the email address where you want to receive arXiV subscriptions

And you're good to go!

In order to change your subscription services, change the list at the top of `daily_preprint.py`. Emails go out at 5:00 UTC (midnight ET).
