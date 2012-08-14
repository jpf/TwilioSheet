from pyquery import PyQuery as pq
import urllib
import re

class GFormException(Exception):
    pass

class GForm:
    formkey = ''
    """String containing the value of the formkey GET paramater from a Google Form URL"""
    action_url = ''
    """String containing the URL value from the 'action' attribute of the <form> tag in a Google Form"""
    parameters = {}
    """Dictionary where the 'key' is the input name and the 'value' is the default value, if any"""
    labels = {}
    """Dictionary where the 'key' is the label for a Google Form input and the 'value' is the input name"""

    def __init__(self, formkey):
        """Given a Google Form 'formkey', will parse interesting information from said form."""
        form_url = "https://docs.google.com/spreadsheet/viewform?formkey=%s" % formkey
        self.formkey = ''
        self.action_url = ''
        self.parameters = {}
        self.labels = {}
        try:
            d = pq(url=form_url)
        except:
            raise GFormException("""

Error parsing URL '%s', did you pass the correct formkey?""")
        
        form = d('#ss-form')
        # Define parameters with default values, if any
        for item in d('#ss-form input'):
            self.parameters[item.name] = item.value
        # Map out the label to form-input-name relationships
        for item in d.find('div.ss-form-entry'):
            elements = list(item)
            if not elements[0].tag == 'label':
                continue
            input_label = elements[0].text.rstrip()
            input_id    = elements[2].name
            self.labels[input_label] = input_id
        self.action_url = form.attr['action']

    def show_state(self):
        """Print the contents of the 'paramaters' and 'labels' properties"""
        print "Parameters:",
        print self.parameters
        print "Labels:",
        print self.labels

    def submit(self):
        """Submit the contents of the 'parameters' property to the Google Form"""
        f = urllib.urlopen(self.action_url, urllib.urlencode(self.parameters))
        form_submission_result = f.read()
        if re.search(r'Create your own form', form_submission_result):
            message = "Submitted successfully!"
            # print message
            return message
        message = "Error submitting to form."
        # print message
        return message

