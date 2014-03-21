from pyquery import PyQuery as pq
import urllib
import re


class GFormException(Exception):
    pass


class GForm:
    formkey = ''
    """String containing the value
       of the formkey GET paramater from a Google Form URL"""
    action_url = ''
    """String containing the URL value
       from the 'action' attribute of the <form> tag in a Google Form"""
    parameters = {}
    """Dictionary where the 'key' is the input name
       and the 'value' is the default value, if any"""
    labels = {}
    """Dictionary where the 'key' is the label
       for a Google Form input and the 'value' is the input name"""

    def __init__(self, formkey, url=None):
        """Given a Google Form 'formkey',
           will parse interesting information from said form."""
        self.form_url = url
        self.formkey = ''
        self.action_url = ''
        self.parameters = {}
        self.labels = {}
        try:
            d = pq(url=self.form_url)
        except:
            raise GFormException("""

Error parsing URL '%s', did you pass the correct formkey?""")

        form = d('#ss-form')
        # Define parameters with default values, if any
        # Map out the label to form-input-name relationships
        for item in d('.ss-form-entry input'):
            self.parameters[item.name] = item.value
            input_label = item.get('aria-label')
            if input_label:
              input_id = item.get('name')
              self.labels[input_label.strip( )] = input_id
        self.action_url = form.attr['action']

    def show_state(self):
        """Print the contents of the 'paramaters' and 'labels' properties"""
        print "Parameters:",
        print self.parameters
        print "Labels:",
        print self.labels

    def submit(self):
        """Submit the contents of the 'parameters' property
           to the Google Form"""
        f = urllib.urlopen(self.action_url, urllib.urlencode(self.parameters))
        form_submission_result = f.read()
        message = "Error submitting to form."
        if re.search(r'Create your own form', form_submission_result):
            message = "Submitted successfully!"
        # http://bit.ly/12ySdJQ
        response = "<Response><!-- %s --></Response>" % message
        return response
