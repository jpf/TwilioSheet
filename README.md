# Twilio-SMS-to-Google-Form

A Python Flask application to take Twilio SMSes and submit them to a Google Form

This is a work in progress but you can use it now if you know what you are doing:

1. Make a Google Form (http://support.google.com/docs/bin/answer.py?hl=en&answer=87809)
2. Add items to your form where the "Question Title" is a parameter name for a TwiML SMS Request (http://www.twilio.com/docs/api/twiml/sms/twilio_request) For example: To, From, Body
3. At the bottom of the "Edit form" window, look for the text "You can view the published form here". 
4. Copy the form key from the URL that is after the text in the step above, the form key is the string of x'es in the the URL that looks this: https://docs.google.com/a/twilio.com/spreadsheet/viewform?formkey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
5. Run this code somewhere (Heroku? Run it on your machine and use localtunnel?)
6. Make a URL with the form key in this format: http://[path to the host for this code]/form/[form key you got in step 4]
7. Use the URL from the step above as the "SMS Request URL" for one of your Twilio numbers.

## Setup virtualenv

    $ virtualenv venv --distribute
    $ source venv/bin/activate
    $ pip install -r requirements

## How to deploy to Heroku

    $ heroku create
    $ git push heroku master

See also: https://devcenter.heroku.com/articles/python/
