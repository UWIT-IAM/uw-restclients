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
from restclients.models.sws import Person, Curriculum, Department, College, Term


class SWSv4VSv5Test(TestCase):
    def test_get_sections_by_instructor_and_term(self):
        t1 = t2 = Term(quarter="summer", year=2013)
        i = Person(uwregid="FBB38FE46A7C11D5A4AE0004AC494FFE")

        self.assertTrue(is_obj_list_eq(v4_get_sections_by_instructor_and_term(i, t1), v5_get_sections_by_instructor_and_term(i, t2)))

    def test_get_sections_by_delegate_and_term(self):
        t1 = t2 = Term(quarter="summer", year=2013)
        d = Person(uwregid="FBB38FE46A7C11D5A4AE0004AC494FFE")

        self.assertTrue(is_obj_list_eq(v4_get_sections_by_delegate_and_term(d, t1), v5_get_sections_by_delegate_and_term(d, t2)))

    def test_get_sections_by_curriculum_and_term(self):
        t1 = t2 = Term(quarter="winter", year=2013)
        c = Curriculum(label="ENDO")
        self.assertTrue(is_obj_list_eq(v4_get_sections_by_curriculum_and_term(c, t1), v5_get_sections_by_curriculum_and_term(c, t2)))

    def test_get_section_by_url(self):
        u1 = "/student/v4/course/2013,summer,MATH,125/G.json"
        u2 = "/student/v5/course/2013,summer,MATH,125/G.json"
        self.assertTrue(is_obj_list_eq(v4_get_section_by_url(u1), v5_get_section_by_url(u2)))

    def test_get_section_by_label(self):
        label = "2013,summer,B BIO,180/A"
        self.assertTrue(is_obj_list_eq(v4_get_section_by_label(label), v5_get_section_by_label(label)))

    def test_get_linked_sections(self):
        s1 = v4_get_section_by_label("2013,summer,TRAIN,100/A")
        s2 = v5_get_section_by_label("2013,summer,TRAIN,100/A")
        self.assertTrue(is_obj_list_eq(v4_get_linked_sections(s1), v5_get_linked_sections(s2)))

    def test_get_joint_sections(self):
        s1 = v4_get_section_by_label("2013,winter,ASIAN,203/A")
        s2 = v5_get_section_by_label("2013,winter,ASIAN,203/A")
        self.assertTrue(is_obj_list_eq(v4_get_joint_sections(s1), v5_get_joint_sections(s2)))

# XXX - no access to the graderoster resource
#    def test_get_graderoster(self):
#        self.assertTrue(is_obj_list_eq(v4_get_graderoster(), v5_get_graderoster()))
#
#    def test_update_graderoster(self):
#        self.assertTrue(is_obj_list_eq(v4_update_graderoster(), v5_update_graderoster()))
#
#    def test_graderoster_from_xhtml(self):
#        self.assertTrue(is_obj_list_eq(v4_graderoster_from_xhtml(), v5_graderoster_from_xhtml()))

    def test_get_all_campuses(self):
        self.assertTrue(is_obj_list_eq(v4_get_all_campuses(), v5_get_all_campuses()))

    def test_get_all_colleges(self):
        self.assertTrue(is_obj_list_eq(v4_get_all_colleges(), v5_get_all_colleges()))

    def test_get_curricula_by_department(self):
        d = Department(label="EDUC")
        self.assertTrue(is_obj_list_eq(v4_get_curricula_by_department(d), v5_get_curricula_by_department(d)))

    def test_get_curricula_by_term(self):
        t1 = t2 = Term(quarter='winter', year=2013)
        self.assertTrue(is_obj_list_eq(v4_get_curricula_by_term(t1), v5_get_curricula_by_term(t2)))

    def test_get_departments_by_college(self):
        c = College(label="MED")
        self.assertTrue(is_obj_list_eq(v4_get_departments_by_college(c), v5_get_departments_by_college(c)))

    def test_get_term_by_year_and_quarter(self):
        self.assertTrue(is_obj_list_eq(v4_get_term_by_year_and_quarter(2013, "spring"), v5_get_term_by_year_and_quarter(2013, "spring")))

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

    # No v4 resource!
#    def test_get_account_balances_by_regid(self):
#        self.assertTrue(is_obj_list_eq(v4_get_account_balances_by_regid(), v5_get_account_balances_by_regid()))

    def test_get_grades_by_regid_and_term(self):
        t1 = v4_get_current_term()
        t2 = v5_get_current_term()
        r = "9136CCB8F66711D5BE060004AC494FFE"
        self.assertTrue(is_obj_list_eq(v4_get_grades_by_regid_and_term(r, t1), v5_get_grades_by_regid_and_term(r, t2)))

    def test_get_enrollment_by_regid_and_term(self):
        t1 = v4_get_current_term()
        t2 = v5_get_current_term()
        r = "9136CCB8F66711D5BE060004AC494FFE"
        self.assertTrue(is_obj_list_eq(v4_get_enrollment_by_regid_and_term(r, t1), v5_get_enrollment_by_regid_and_term(r, t2)))

    def test_get_section_status_by_label(self):
        l = '2012,autumn,CSE,100/W'
        print v5_get_section_status_by_label(l)
        self.assertTrue(is_obj_list_eq(v4_get_section_status_by_label(l), v5_get_section_status_by_label(l)))

    def test_get_active_registrations_by_section(self):
        s1 = v4_get_section_by_label("2013,winter,DROP_T,100/A")
        s2 = v5_get_section_by_label("2013,winter,DROP_T,100/A")

        self.assertTrue(is_obj_list_eq(v4_get_active_registrations_by_section(s1), v5_get_active_registrations_by_section(s2), order_list_by="person", nested_order_by="uwregid"))

    def test_get_all_registrations_by_section(self):
        s1 = v4_get_section_by_label("2013,winter,DROP_T,100/A")
        s2 = v5_get_section_by_label("2013,winter,DROP_T,100/A")
        self.assertTrue(is_obj_list_eq(v4_get_all_registrations_by_section(s1), v5_get_all_registrations_by_section(s2), order_list_by="person", nested_order_by="uwregid"))

    def test_get_credits_by_section_and_regid(self):
        s1 = v4_get_section_by_label("2012,summer,PHYS,121/A")
        s2 = v5_get_section_by_label("2012,summer,PHYS,121/A")
        r = "9136CCB8F66711D5BE060004AC494FFE"
        self.assertTrue(is_obj_list_eq(v4_get_credits_by_section_and_regid(s1, r), v5_get_credits_by_section_and_regid(s2, r)))

    def test_get_schedule_by_regid_and_term(self):
        t1 = v4_get_current_term()
        t2 = v5_get_current_term()
        r = "9136CCB8F66711D5BE060004AC494FFE"

        self.assertTrue(is_obj_list_eq(v4_get_schedule_by_regid_and_term(r, t1), v5_get_schedule_by_regid_and_term(r, t2)))

# Helper to test list of objects for equality

import warnings
from django.db import models
from datetime import date, datetime
from decimal import Decimal
def is_obj_list_eq(a, b, order_list_by=None, nested_order_by=None):
    if type(a) != type(b):
        warnings.warn("Typeof %s doesn't equal type of %s" % (a, b))
        return False

    if type(a) == type([]):
        if len(a) != len(b):
            print "Len A: ", len(a), " Len b: ", len(b)
            warnings.warn("Length of a != b")
            return False

        if order_list_by is not None:
            if nested_order_by is not None:
                if len(a) > 0 and hasattr(a[0], order_list_by) and hasattr(getattr(a[0], order_list_by), nested_order_by):
                        a.sort(key=lambda x: getattr(getattr(x, order_list_by), nested_order_by))
                        b.sort(key=lambda x: getattr(getattr(x, order_list_by), nested_order_by))
            else:
                if len(a) > 0 and hasattr(a[0], order_list_by):
                    a.sort(key=lambda x: getattr(x, order_list_by))
                    b.sort(key=lambda x: getattr(x, order_list_by))

        for i in range(len(a)):
            if not is_obj_list_eq(a[i], b[i]):
                return False

        return True

    elif type(a) == type("") or type(a) == type(u""):
        # Some attributes have the url fragment in them :(
        a = a.replace("v4", "__version__")
        b = b.replace("v4", "__version__")
        a = a.replace("v5", "__version__")
        b = b.replace("v5", "__version__")
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

    elif type(a) == type(True):
        return a == b

    elif type(a) == type(0):
        if a == b:
            return True
        return False

    elif type(a) == type(date(2014, 1, 1)):
        return a == b

    elif type(a) == type(datetime(2014, 1, 1)):
        return a == b

    elif type(a) == type(Decimal(0)):
        return a == b

    else:
        try:
            for k in [f.name for f in a._meta.fields]:
                if not hasattr(a, k) and not hasattr(b, k):
                    pass
                elif not is_obj_list_eq(getattr(a, k), getattr(b, k)):
                    return False

            return True
        except Exception as ex:
            warnings.warn("Err: %s" % ex)
            return False

    return True
