from django.test import TestCase
from django.conf import settings
from restclients.bookstore import Bookstore
from restclients.sws import SWS


class BookstoreScheduleTest(TestCase):
    def test_sched(self):
        with self.settings(
            RESTCLIENTS_BOOK_DAO_CLASS='restclients.dao_implementation.book.File',
            RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File',
            ):

            sws = SWS()
            books = Bookstore()

            term = sws.get_current_term()
            schedule = sws.schedule_for_regid_and_term('AA36CCB8F66711D5BE060004AC494FFE', term)

            book_data = books.get_books_for_schedule(schedule)

            self.assertEquals(len(book_data), 2, "Has data for 2 sections")

            self.assertEquals(len(book_data["13830"]), 0, "No books for sln 13830")
            self.assertEquals(len(book_data["13833"]), 1, "one book for sln 13833")

            book = book_data["13833"][0]

            self.assertEquals(book.price, 175.00, "Has the right book price")


