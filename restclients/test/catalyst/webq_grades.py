from django.test import TestCase
from restclients.catalyst.webq import WebQ

class CatalystWebQGrades(TestCase):

   def test_student_grades(self):
         with self.settings(
                RESTCLIENTS_CATALYST_DAO_CLASS='restclients.dao_implementation.catalyst.File',
                RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File',
                RESTCLIENTS_PWS_DAO_CLASS='restclients.dao_implementation.pws.File'):

                catalyst = WebQ()
                data = catalyst.get_grades_for_student_and_term('javerage', 2013, 'Autumn')

                train = data['2013,autumn,TRAIN,100/A']

                self.assertEquals(train[0].class_grade, '')
                self.assertEquals(train[0].url, '')

                self.assertEquals(len(train[0].items), 1)
                self.assertEquals(train[0].items[0].name, "Quiz 1")
                self.assertEquals(train[0].items[0].url, "https://catalyst.uw.edu/webq/survey/fake/999")
                self.assertEquals(train[0].items[0].score, 10)
                self.assertEquals(train[0].items[0].max_points, 20)


   def test_student_grades_2_quizzes(self):
         with self.settings(
                RESTCLIENTS_CATALYST_DAO_CLASS='restclients.dao_implementation.catalyst.File',
                RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File',
                RESTCLIENTS_PWS_DAO_CLASS='restclients.dao_implementation.pws.File'):

                catalyst = WebQ()
                data = catalyst.get_grades_for_student_and_term('javerage', 2013, 'Spring')




