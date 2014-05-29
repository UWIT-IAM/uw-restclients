from django.test import TestCase
from django.conf import settings
from restclients.library.mylibinfo import get_account, get_account_html
from restclients.exceptions import DataFailureException

class MyLibInfoTest(TestCase):

    def test_get_account(self):
        with self.settings(
            RESTCLIENTS_LIBRARIES_DAO_CLASS =
            'restclients.dao_implementation.libraries.File'):

            account = get_account("javerage")
            self.assertEquals(account.next_due, "2014-05-27")
            self.assertEquals(account.holds_ready, 1)
            self.assertEquals(account.fines, 5.35)
            self.assertEquals(account.items_loaned, 3)

            account = get_account("jnewstudent")
            self.assertIsNone(account.next_due)
            self.assertEquals(account.holds_ready, 0)
            self.assertEquals(account.fines, 0.0)
            self.assertEquals(account.items_loaned, 0)


    def test_html_response(self):
        with self.settings(
            RESTCLIENTS_LIBRARIES_DAO_CLASS =
            'restclients.dao_implementation.libraries.File'):

            response = get_account_html("javerage")
            self.assertEquals(response, '<p>You have 7 items checked out.<br>\nYou have items due back on 2014-04-29.<br>\nYou don\'t owe any fines.</p>\n<a href="http://alliance-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/dlBasketGet.do?vid=UW&redirectTo=myAccount">Go to your account</a>')


    def test_invalid_user(self):
        with self.settings(
            RESTCLIENTS_LIBRARIES_DAO_CLASS =
            'restclients.dao_implementation.libraries.File'):

            #Testing error message in a 200 response
            self.assertRaises(DataFailureException, get_account, "invalidnetid")
            #Testing non-200 response
            self.assertRaises(DataFailureException, get_account, "invalidnetid123")

            try:
                get_account("invalidnetid")
            except DataFailureException as ex:
                self.assertEquals(ex.msg, "[Alma] User not found/401651")


    def test_with_timestamp(self):
        with self.settings(
            RESTCLIENTS_LIBRARIES_DAO_CLASS=
            'restclients.dao_implementation.libraries.File'):

            response = get_account_html('javerage', timestamp=1391122522900)
            self.assertEquals(response, '<p>You have 7 items checked out.<br>\n You have items due back on 2014-04-29.<br>\n You don\'t owe any fines.</p>\n <a href="http://alliance-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/dlBasketGet.do?vid=UW&amp;redirectTo=myAccount">Go to your account</a>')
