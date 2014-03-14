from django.test import TestCase
from django.conf import settings
import restclients.sws.section as SectionSws
from restclients.models.sws import Term, Curriculum, Person
from restclients.exceptions import DataFailureException, InvalidSectionID

class SWSTestSectionStatusData(TestCase):
    def test_section_by_label(self):
        with self.settings(
                RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File',
                RESTCLIENTS_PWS_DAO_CLASS='restclients.dao_implementation.pws.File'):

            #Valid data, shouldn't throw any exceptions
            section_status = SectionSws.get_section_status_by_label('2012,autumn,CSE,100/W')

            self.assertFalse(section_status.add_code_required)
            self.assertEquals(section_status.current_enrollment, 305)
            self.assertEquals(section_status.current_registration_period, 3)
            self.assertFalse(section_status.faculty_code_required)
            self.assertEquals(section_status.limit_estimated_enrollment, 345)
            self.assertEquals(section_status.limit_estimate_enrollment_indicator, 'limit')
            self.assertEquals(section_status.room_capacity, 345)
            self.assertEquals(section_status.sln, 12588)
            self.assertEquals(section_status.space_available, 40)
            self.assertEquals(section_status.is_open, True)
