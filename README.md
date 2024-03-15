# arxiv-email

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/tbrazel/arxiv-email/math-email.yml)
 
This repo contains a bot, which sends daily HTML-formatted arXiv emails

<img width="667" alt="arxiv-email" src="https://github.com/tbrazel/arxiv-email/assets/42276623/082de276-3624-4b3e-9e87-97426b165aff">

# Installation

1. Fork this repository
2. Make sure you have your gmail credentials ready to go. It may not work unless you set up a [new app password](https://support.google.com/mail/answer/185833?hl=en-GB) on gmail (if you can't find this, use "Search Google Account").
3. In your forked repository, go to Settings > Secrets and variables > Actions, and add your credentials securely there. Create three Repository Secrets:
* `GMAIL_USER` - this is the email that will send your daily emails
* `GMAIL_PASSWORD` - the app password for that email
* `RECIPIENT` - the email address where you want to receive arXiV subscriptions
4. In `.github/workflows/math-email.yml` remove the last step, i.e. everything at/below "`- name: freeloaders`". You can also safely remove the file `freeloaders.py`. This is for me to send arxiv emails to friends who are too lazy to fork this repo 😃

And you're good to go!

In order to change your subscription services, change the `subscriptions` variable in `daily_preprint.py`. Emails go out at 5:00 UTC (midnight ET).
