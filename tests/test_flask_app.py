import os
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
import app
import gform

# From: http://code.activestate.com/recipes/52256-check-xml-well-formedness/
def is_xml_like(input):
    if input.startswith('<') and input.endswith('>'):
        return True
    else:
        print "This does not appear to be XML: '%s'" % input
        return False

def mock_urlopen(action_url, parameters):
    class MockUrllib:
        def read(self):
            return "Create your own form"

    return MockUrllib()

def mock_init(self, string):
    return None

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.tearDown()
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_has_default_route(self):
        path = "/"
        rv = self.app.get(path)
        self.assertEquals(rv.status, "200 OK")

    def test_default_route_returns_some_html(self):
        path = "/"
        rv = self.app.get(path)
        self.assertIn("<html", rv.data)

    def test_post_to_form_returns_xml(self):
        gform.GForm.__init__ = mock_init
        gform.urllib.urlopen = mock_urlopen
        path = "/form/aBCdEfG0hIJkLM1NoPQRStuvwxYZAbc2DE"
        return_text = self.app.post(path).data
        rv = is_xml_like(return_text)
        self.assertEquals(True, rv)
