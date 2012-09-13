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
6. If you see an option that reads "Require [Company Name] sign-in to view this form.", uncheck the box for that option.
7. Type "Testing" in the box that says "You can include any text or info that will help people fill this out."
8. Click "Save"
9. Click on the URL at the bottom of the window.

   ![Enter "testing" in the description box, click the "Save" button, click on the URL at the bottom of the window](http://twiliosheet.herokuapp.com/static/img/4-save-form.png)

9. Another window will open. Copy the URL from the location bar of that window:

   ![Copy the URL from the window with the Google Form you just created](http://twiliosheet.herokuapp.com/static/img/5-copy-url.png)
10. Open [TwilioSheet](http://twiliosheet.herokuapp.com) in a new window.
11. Paste that URL you copied in step 9 into the box on TwilioSheet, then click the "Submit" button.
12. You should get a response from the site saying "It worked!"
13. Copy that URL.

**Open another window, in that new window:**

1. Log in to your Twilio account.
2. Go to the "Numbers" section of your Twilio account (or click here)
3. Click on the number you want to set up to send SMS data to your Google Spreadsheet.
5. Paste the URL you copied in step 13 (above) into the "SMS Request URL" box for the Twilio number you are configuring.
6. Make sure that the dropdown to the right of the "SMS Request URL" box is set to "POST".
7. Click the "Save Changes" button.

   ![Example of a Twilio number being configured](http://twiliosheet.herokuapp.com/static/img/6-paste-url.png)

8. Send a text message that says "test" to the number you just set up.

**In your Google Spreadsheet:**

1. Any text message you send to your Twilio number should show up in the Google Spreadsheet you set up after a delay of about 5-10 seconds.
2. Start writing formulas to process the incomming text messages.

tl;dr:
------

1. Make a Google Form (http://support.google.com/docs/bin/answer.py?hl=en&answer=87809)
2. Add items to your form where the "Question Title" is a parameter name for a TwiML SMS Request (http://www.twilio.com/docs/api/twiml/sms/twilio_request) For example: To, From, Body
3. Publish your form.
4. At the bottom of the "Edit form" window, look for the text "You can view the published form here". 
5. Copy the URL in the step above. Paste it into the box on [TwilioSheet](http://twiliosheet.herokuapp.com).
6. TwilioSheet will make a new URL for you, use that URL as the "SMS Request URL" for one of your Twilio numbers.

Notes:

You can run this code yourself if you like. Here are tips on how to do that:

**To deploy to Heroku, you'll need to set up virtualenv, like so:**

    $ virtualenv venv --distribute
    $ source venv/bin/activate
    $ pip install -r requirements

**After setting up virtualenv, this is how you deploy to Heroku**

    $ heroku create
    $ git push heroku master

See also: https://devcenter.heroku.com/articles/python/

