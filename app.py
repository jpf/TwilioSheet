from pyquery import PyQuery as pq
import urllib
import re
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def note():
    return "Send SMSes to the /form route"

@app.route("/form/<form_key>", methods=['GET', 'POST'])
def form(form_key):
    form_url = "https://docs.google.com/a/twilio.com/spreadsheet/viewform?formkey=%s" % form_key
    d = pq(url=form_url)
    form = d('#ss-form')
    entries = d.find('div.ss-form-entry')
    # I should really pull these from the form directly
    parameters = {'pageNumber': '0',
                  'backupCache': '',
                  'submit': 'Submit'}

    for div in entries:
        elements = list(div)
        if not elements[0].tag == 'label':
            continue
        input_label = elements[0].text.rstrip()
        input_id    = elements[2].name
        try:
            parameters[input_id] = request.form[input_label]
        except:
            pass

    print request.form
    print parameters
    # form_input

    print "action=%s" % form.attr['action']
    google_form = form.attr['action']

    f = urllib.urlopen(google_form, urllib.urlencode(parameters))
    result = f.read()
    if re.search(r'Create your own form', result):
        message = "Submitted successfully!"
        print message
        return message
    message = "Error submitting to form."
    print message
    return message

if __name__ == "__main__":
    app.run()
    
