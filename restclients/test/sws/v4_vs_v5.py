from restclients.sws.v4.section import get_sections_by_instructor_and_term as v4_get_sections_by_instructor_and_term
from restclients.sws.v5.section import get_sections_by_instructor_and_term as v5_get_sections_by_instructor_and_term
from restclients.sws.v4.section import get_sections_by_delegate_and_term as v4_get_sections_by_delegate_and_term
from restclients.sws.v5.section import get_sections_by_delegate_and_term as v5_get_sections_by_delegate_and_term
from restclients.sws.v4.section import get_sections_by_curriculum_and_term as v4_get_sections_by_curriculum_and_term
from restclients.sws.v5.section import get_sections_by_curriculum_and_term as v5_get_sections_by_curriculum_and_term
from restclients.sws.v4.section import get_section_by_url as v4_get_section_by_url
from restclients.sws.v5.section import get_section_by_url as v5_get_section_by_url
from restclients.sws.v4.section import get_section_by_label as v4_get_section_by_label
from restclients.sws.v5.section import get_section_by_label as v5_get_section_by_label
from restclients.sws.v4.section import get_linked_sections as v4_get_linked_sections
from restclients.sws.v5.section import get_linked_sections as v5_get_linked_sections
from restclients.sws.v4.section import get_joint_sections as v4_get_joint_sections
from restclients.sws.v5.section import get_joint_sections as v5_get_joint_sections
from restclients.sws.v4.notice import get_notices_by_regid as v4_get_notices_by_regid
from restclients.sws.v5.notice import get_notices_by_regid as v5_get_notices_by_regid
from restclients.sws.v4.graderoster import get_graderoster as v4_get_graderoster
from restclients.sws.v5.graderoster import get_graderoster as v5_get_graderoster
from restclients.sws.v4.graderoster import update_graderoster as v4_update_graderoster
from restclients.sws.v5.graderoster import update_graderoster as v5_update_graderoster
from restclients.sws.v4.graderoster import graderoster_from_xhtml as v4_graderoster_from_xhtml
from restclients.sws.v5.graderoster import graderoster_from_xhtml as v5_graderoster_from_xhtml
from restclients.sws.v4.campus import get_all_campuses as v4_get_all_campuses
from restclients.sws.v5.campus import get_all_campuses as v5_get_all_campuses
from restclients.sws.v4.college import get_all_colleges as v4_get_all_colleges
from restclients.sws.v5.college import get_all_colleges as v5_get_all_colleges
from restclients.sws.v4.curriculum import get_curricula_by_department as v4_get_curricula_by_department
from restclients.sws.v5.curriculum import get_curricula_by_department as v5_get_curricula_by_department
from restclients.sws.v4.curriculum import get_curricula_by_term as v4_get_curricula_by_term
from restclients.sws.v5.curriculum import get_curricula_by_term as v5_get_curricula_by_term
from restclients.sws.v4.department import get_departments_by_college as v4_get_departments_by_college
from restclients.sws.v5.department import get_departments_by_college as v5_get_departments_by_college
from restclients.sws.v4.term import get_term_by_year_and_quarter as v4_get_term_by_year_and_quarter
from restclients.sws.v5.term import get_term_by_year_and_quarter as v5_get_term_by_year_and_quarter
from restclients.sws.v4.term import get_current_term as v4_get_current_term
from restclients.sws.v5.term import get_current_term as v5_get_current_term
from restclients.sws.v4.term import get_next_term as v4_get_next_term
from restclients.sws.v5.term import get_next_term as v5_get_next_term
from restclients.sws.v4.term import get_previous_term as v4_get_previous_term
from restclients.sws.v5.term import get_previous_term as v5_get_previous_term
from restclients.sws.v4.term import get_term_before as v4_get_term_before
from restclients.sws.v5.term import get_term_before as v5_get_term_before
from restclients.sws.v4.term import get_term_after as v4_get_term_after
from restclients.sws.v5.term import get_term_after as v5_get_term_after
from restclients.sws.v4.financial import get_account_balances_by_regid as v4_get_account_balances_by_regid
from restclients.sws.v5.financial import get_account_balances_by_regid as v5_get_account_balances_by_regid
from restclients.sws.v4.enrollment import get_grades_by_regid_and_term as v4_get_grades_by_regid_and_term
from restclients.sws.v5.enrollment import get_grades_by_regid_and_term as v5_get_grades_by_regid_and_term
from restclients.sws.v4.enrollment import get_enrollment_by_regid_and_term as v4_get_enrollment_by_regid_and_term
from restclients.sws.v5.enrollment import get_enrollment_by_regid_and_term as v5_get_enrollment_by_regid_and_term
from restclients.sws.v4.section_status import get_section_status_by_label as v4_get_section_status_by_label
from restclients.sws.v5.section_status import get_section_status_by_label as v5_get_section_status_by_label
from restclients.sws.v4.registration import get_active_registrations_by_section as v4_get_active_registrations_by_section
from restclients.sws.v5.registration import get_active_registrations_by_section as v5_get_active_registrations_by_section
from restclients.sws.v4.registration import get_all_registrations_by_section as v4_get_all_registrations_by_section
from restclients.sws.v5.registration import get_all_registrations_by_section as v5_get_all_registrations_by_section
from restclients.sws.v4.registration import get_credits_by_section_and_regid as v4_get_credits_by_section_and_regid
from restclients.sws.v5.registration import get_credits_by_section_and_regid as v5_get_credits_by_section_and_regid
from restclients.sws.v4.registration import get_schedule_by_regid_and_term as v4_get_schedule_by_regid_and_term
from restclients.sws.v5.registration import get_schedule_by_regid_and_term as v5_get_schedule_by_regid_and_term
from django.test import TestCase


class SWSv4VSv5Test(TestCase):
    def test_get_sections_by_instructor_and_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_sections_by_instructor_and_term(), v5_get_sections_by_instructor_and_term()))

    def test_get_sections_by_delegate_and_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_sections_by_delegate_and_term(), v5_get_sections_by_delegate_and_term()))

    def test_get_sections_by_curriculum_and_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_sections_by_curriculum_and_term(), v5_get_sections_by_curriculum_and_term()))

    def test_get_section_by_url(self):
        self.assertTrue(is_obj_list_eq(v4_get_section_by_url(), v5_get_section_by_url()))

    def test_get_section_by_label(self):
        self.assertTrue(is_obj_list_eq(v4_get_section_by_label(), v5_get_section_by_label()))

    def test_get_linked_sections(self):
        self.assertTrue(is_obj_list_eq(v4_get_linked_sections(), v5_get_linked_sections()))

    def test_get_joint_sections(self):
        self.assertTrue(is_obj_list_eq(v4_get_joint_sections(), v5_get_joint_sections()))

    def test_get_notices_by_regid(self):
        self.assertTrue(is_obj_list_eq(v4_get_notices_by_regid(), v5_get_notices_by_regid()))

    def test_get_graderoster(self):
        self.assertTrue(is_obj_list_eq(v4_get_graderoster(), v5_get_graderoster()))

    def test_update_graderoster(self):
        self.assertTrue(is_obj_list_eq(v4_update_graderoster(), v5_update_graderoster()))

    def test_graderoster_from_xhtml(self):
        self.assertTrue(is_obj_list_eq(v4_graderoster_from_xhtml(), v5_graderoster_from_xhtml()))

    def test_get_all_campuses(self):
        self.assertTrue(is_obj_list_eq(v4_get_all_campuses(), v5_get_all_campuses()))

    def test_get_all_colleges(self):
        self.assertTrue(is_obj_list_eq(v4_get_all_colleges(), v5_get_all_colleges()))

    def test_get_curricula_by_department(self):
        self.assertTrue(is_obj_list_eq(v4_get_curricula_by_department(), v5_get_curricula_by_department()))

    def test_get_curricula_by_term(self):
        t1 = v4_get_current_term()
        t2 = v5_get_current_term()
        self.assertTrue(is_obj_list_eq(v4_get_curricula_by_term(t1), v5_get_curricula_by_term(t2)))

    def test_get_departments_by_college(self):
        self.assertTrue(is_obj_list_eq(v4_get_departments_by_college(), v5_get_departments_by_college()))

    def test_get_term_by_year_and_quarter(self):
        self.assertTrue(is_obj_list_eq(v4_get_term_by_year_and_quarter(), v5_get_term_by_year_and_quarter()))

    def test_get_current_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_current_term(), v5_get_current_term()))

    def test_get_next_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_next_term(), v5_get_next_term()))

    def test_get_previous_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_previous_term(), v5_get_previous_term()))

    def test_get_term_before(self):
        t1 = v4_get_current_term()
        t2 = v5_get_current_term()
        self.assertTrue(is_obj_list_eq(v4_get_term_before(t1), v5_get_term_before(t2)))

    def test_get_term_after(self):
        t1 = v4_get_current_term()
        t2 = v5_get_current_term()
        self.assertTrue(is_obj_list_eq(v4_get_term_after(t1), v5_get_term_after(t2)))

    def test_get_account_balances_by_regid(self):
        self.assertTrue(is_obj_list_eq(v4_get_account_balances_by_regid(), v5_get_account_balances_by_regid()))

    def test_get_grades_by_regid_and_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_grades_by_regid_and_term(), v5_get_grades_by_regid_and_term()))

    def test_get_enrollment_by_regid_and_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_enrollment_by_regid_and_term(), v5_get_enrollment_by_regid_and_term()))

    def test_get_section_status_by_label(self):
        self.assertTrue(is_obj_list_eq(v4_get_section_status_by_label(), v5_get_section_status_by_label()))

    def test_get_active_registrations_by_section(self):
        self.assertTrue(is_obj_list_eq(v4_get_active_registrations_by_section(), v5_get_active_registrations_by_section()))

    def test_get_all_registrations_by_section(self):
        self.assertTrue(is_obj_list_eq(v4_get_all_registrations_by_section(), v5_get_all_registrations_by_section()))

    def test_get_credits_by_section_and_regid(self):
        self.assertTrue(is_obj_list_eq(v4_get_credits_by_section_and_regid(), v5_get_credits_by_section_and_regid()))

    def test_get_schedule_by_regid_and_term(self):
        self.assertTrue(is_obj_list_eq(v4_get_schedule_by_regid_and_term(), v5_get_schedule_by_regid_and_term()))

# Helper to test list of objects for equality

import warnings
from django.db import models
def is_obj_list_eq(a, b):
    if type(a) != type(b):
        warnings.warn("Typeof %s doesn't equal type of %s" % (a, b))
        return False

    if type(a) == type([]):
        if len(a) != len(b):
            warnings.warn("Length of a != b")
            return False

        for i in range(len(a)):
            if not is_obj_list_eq(a[i], b[i]):
                return False

        return True

    elif type(a) == type("") or type(a) == type(u""):
        if a == b:
            return True
        warnings.warn("Not equal: %s, %s" % (a, b))
        return False

    elif type(a) == type({}):
        for key in a:
            if not is_obj_list_eq(a[key], b[key]):
                return False
        return True

    elif type(a) == type(None):
        return True


    else:
        try:
            for k in [f.name for f in a._meta.fields]:
                if not is_obj_list_eq(getattr(a, k), getattr(b, k)):
                    return False

            return True
        except Exception as ex:
            print "Err: ", ex

    return True
    

