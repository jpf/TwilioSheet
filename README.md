Receive Twilio SMS messages in a Google Spreadsheet
===================================================

Use Twilio and Google Spreadsheets to build your own applications to do SMS polling / SMS voting, keyword marketing data collection, expense tracking, time tracking, and more.

No programming experience required.


Instructions:
-------------

_(looking for a tl;dr? See below)_

![An example spreadsheet](http://twiliosheet.herokuapp.com/static/img/twiliosheet-example.png)

Get Started
-----------

1. [Create a Google Spreadsheet](http://support.google.com/docs/bin/answer.py?hl=en&answer=87809):

   ![Create > Spreadsheet](http://twiliosheet.herokuapp.com/static/img/1-create-spreadsheet.png)

2. Name the spreadsheet "TwilioSheet" (or any name of your choosing)
3. Add "SmsSid", "To", "From", and "Body" to the first line in your new spreadsheet ([other parameters are avaiable as well](http://www.twilio.com/docs/api/twiml/sms/twilio_request)):

   ![What the Google Spreadsheet should look like after this step](http://twiliosheet.herokuapp.com/static/img/2-name-first-row.png)

4. Click on the "Tools" menu, then click "Create a form":

   ![Tools > Create a form](http://twiliosheet.herokuapp.com/static/img/3-create-a-form.png)

5. A window will open.
6. Type "Testing" in the box that says "You can include any text or info that will help people fill this out."
7. Click "Save"
8. Click on the URL at the bottom of the window.

   ![Enter "testing" in the description box, click the "Save" button, click on the URL at the bottom of the window](http://twiliosheet.herokuapp.com/static/img/4-save-form.png)

9. Another window will open. Copy the URL from the location bar of that window:

   ![Copy the URL from the window with the Google Form you just created](http://twiliosheet.herokuapp.com/static/img/5-copy-url.png)

10. Paste that URL into the box on the site for TwilioSheet, then click the "Submit" button.

11. You should get a response from the site saying "It worked!"

**In another window:**

1. Log in to your Twilio account.
2. Go to the "Numbers" section of your Twilio account (or click here)
3. Click on the number you want to set up to send SMS data to your Google Spreadsheet.
4. Copy the URL you were given by the site.
5. Paste the URL you just copied into the "SMS Request URL" box on the Twilio number you are configuring.
6. Click the "Save Changes" button.

   ![Example of a Twilio number being configured](http://twiliosheet.herokuapp.com/static/img/6-paste-url.png)

7. Send a text message to the number you just set up.

**In your Google Spreadsheet:**

1. Any text message you send to your Twilio number should show up in the Google Spreadsheet you set up after a delay of about 5-10 seconds.
2. Start writing formulas to process the incomming text messages.

tl;dr:
------

1. Make a Google Form (http://support.google.com/docs/bin/answer.py?hl=en&answer=87809)
2. Add items to your form where the "Question Title" is a parameter name for a TwiML SMS Request (http://www.twilio.com/docs/api/twiml/sms/twilio_request) For example: To, From, Body
3. Publish your form.
4. At the bottom of the "Edit form" window, look for the text "You can view the published form here". 
5. Copy the value of the "formkey" paramater from the URL in the step above. (For example, the "formkey" is the string of x'es in this URL: https://docs.google.com/a/twilio.com/spreadsheet/viewform?formkey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
6. Run this code somewhere. I run a copy on Heroku, you should be able to host this anywhere you can run Python though.
7. Make a URL with the form key in this format: http://[path to your host for this code]/form/[form key you got in step 5]
8. Use the URL from the step above as the "SMS Request URL" for one of your Twilio numbers.

Notes:

**To deploy to Heroku, you'll need to set up virtualenv, like so:**

    $ virtualenv venv --distribute
    $ source venv/bin/activate
    $ pip install -r requirements

** After setting up virtualenv, this is how you deploy to Heroku**

    $ heroku create
    $ git push heroku master

See also: https://devcenter.heroku.com/articles/python/

