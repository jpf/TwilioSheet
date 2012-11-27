import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from app import TestURL
from app import NoURLException
from app import NoGoogleInURLException
from app import URLNotForGoogleFormException
from app import URLForGoogleSpreadsheetNotFormException
from app import GoogleFormDoesntExistException
from app import NoTwilioParametersInFormException


# TODO: Use mocking library to simulate HTTP
class TestURLTest(unittest.TestCase):

    def test_requires_url(self):
        url = ''
        with self.assertRaises(NoURLException):
            TestURL(url)

    def test_requires_google_in_url(self):
        for url in ['http://example.com']:
            with self.assertRaises(NoGoogleInURLException):
                TestURL(url)

    def test_not_apparently_for_spreadsheet(self):
        for url in ['https://docs.google.com/spreadsheet/ccc?key=fake#gid=0']:
            with self.assertRaises(URLForGoogleSpreadsheetNotFormException):
                TestURL(url)

    def test_requires_formkey(self):
        for url in ['http://google.com']:
            with self.assertRaises(URLNotForGoogleFormException):
                TestURL(url)

    def test_form_exists(self):
        for url in ['http://google.com?formkey=fake']:
            with self.assertRaises(GoogleFormDoesntExistException):
                TestURL(url)

    def test_form_needs_twilio_parameters(self):
        url = 'https://docs.google.com/spreadsheet/' \
              'viewform?formkey=dHk3N2M5NlAtZV9mMlAyOEU5VE05dEE6MQ'
        with self.assertRaises(NoTwilioParametersInFormException):
            TestURL(url)

    def test_detects_valid_url(self):
        url = 'https://docs.google.com/spreadsheet/' \
              'viewform?formkey=dG02c3hqdEZBaWZMN1NBdnBCZkVzdWc6MQ'
        form = TestURL(url)
        self.assertIsInstance(form.parameters, set)
