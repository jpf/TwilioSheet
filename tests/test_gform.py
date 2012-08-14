import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from gform import GForm, GFormException

class GFormTest(unittest.TestCase):

    def test_true(self):
        self.assertEquals(True, True)

    def test_valid_form(self):
        formkey = 'dG02c3hqdEZBaWZMN1NBdnBCZkVzdWc6MQ'
        gform = GForm(formkey)
        self.assertEquals(gform.__class__.__name__, 'GForm')

    def test_state_not_persisted(self):
        gform = GForm('dG02c3hqdEZBaWZMN1NBdnBCZkVzdWc6MQ')
        self.assertIn('SmsSid', gform.labels)
        self.assertNotIn('One', gform.labels)
        gform = GForm('dHk3N2M5NlAtZV9mMlAyOEU5VE05dEE6MQ')
        self.assertNotIn('SmsSid', gform.labels)
        self.assertIn('One', gform.labels)

    def test_invalid_throws_exception(self):
        formkey = 'invalid_formkey'
        exception_thrown = False
        try:
            GForm(formkey)
        except GFormException:
            exception_thrown = True
        self.assertEquals(exception_thrown, True)
        
