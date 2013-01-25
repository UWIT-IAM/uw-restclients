"""
This is the interface for interacting with the Student Web Service.
"""

from restclients.pws import PWS
from restclients.dao import SWS_DAO
from restclients.models.sws import Term, Section, SectionMeeting
from restclients.models.sws import Registration, ClassSchedule, FinalExam
from restclients.models.sws import Campus, College, Department, Curriculum
from restclients.exceptions import DataFailureException, InvalidSectionID
from urllib import urlencode
from datetime import datetime
import json
import re


class SWS(object):
    """
    The SWS object has methods for getting information
    about courses, and everything related.
    """

    def get_term_by_year_and_quarter(self, year, quarter):
        """
        Returns a restclients.Term object, for the passed year and quarter.
        """
        url = "/student/v4/term/%s,%s.json" % (str(year), quarter.lower())

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        return self._term_from_json(response.data)

    def get_current_term(self):
        """
        Returns a restclients.Term object, for the current term.
        """
        url = "/student/v4/term/current.json"

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        term = self._term_from_json(response.data)

        # A term doesn't become "current" until 2 days before the start of
        # classes.  That's too late to be useful, so if we're after the last
        # day of grade submission window, use the next term resource.
        if datetime.now() > term.grade_submission_deadline:
            return self.get_next_term()

        return term

    def get_next_term(self):
        """
        Returns a restclients.Term object, for the next term.
        """
        url = "/student/v4/term/next.json"

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        return self._term_from_json(response.data)

    def get_previous_term(self):
        """
        Returns a restclients.Term object, for the previous term.
        """
        url = "/student/v4/term/previous.json"

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        return self._term_from_json(response.data)

    def get_sections_by_term_and_curriculum(self, term, curriculum):
        """
        Returns a list of restclients.Section objects for the passed term
        and curriculum.
        """
        url = "/student/v4/section.json?" + urlencode({
            "year": term.year,
            "quarter": term.quarter.lower(),
            "curriculum_abbreviation": curriculum.label})

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        sections = []
        for section_data in data.get("Sections", []):
            url = section_data["Href"]
            response = dao.getURL(url, {"Accept": "application/json"})

            if response.status != 200:
                raise DataFailureException(url, response.status, response.data)

            section = self._section_from_json(response.data)
            sections.append(section)

        return sections

    def get_section_by_label(self, label):
        """
        Returns a restclients.Section object for the passed section label.
        """
        valid = re.compile('^\d{4},'                           # year
                           '(?:winter|spring|summer|autumn),'  # quarter
                           '[\w& ]+,'                          # curriculum
                           '\d{3}\/'                           # course number
                           '[A-Z][A-Z0-9]?$',                  # section id
                           re.VERBOSE)
        if not valid.match(label):
            raise InvalidSectionID(label)

        url = "/student/v4/course/%s.json" % re.sub(r'\s', '%20', label)

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        return self._section_from_json(response.data)

    def get_linked_sections(self, section):
        """
        Returns a list of restclients.Section objects, representing linked
        sections for the passed section.
        """
        dao = SWS_DAO()
        linked_sections = []

        urls = section.linked_section_urls
        for url in urls:
            response = dao.getURL(url, {"Accept": "application/json"})

            if response.status != 200:
                raise DataFailureException(url, response.status, response.data)

            section = self._section_from_json(response.data)
            linked_sections.append(section)

        return linked_sections

    def get_joint_sections(self, section):
        """
        Returns a list of restclients.Section objects, representing joint
        sections for the passed section.
        """
        dao = SWS_DAO()
        joint_sections = []

        urls = section.joint_section_urls
        for url in urls:
            response = dao.getURL(url, {"Accept": "application/json"})

            if response.status != 200:
                raise DataFailureException(url, response.status, response.data)

            section = self._section_from_json(response.data)
            joint_sections.append(section)

        return joint_sections

    def get_all_registrations_for_section(self, section, instructor=None):
        """
        Returns a list of restclients.Registration objects, representing
        all (active and inactive) registrations for the passed section. For
        independent study sections, the passed instructor limits
        registrations to that instructor.
        """
        registrations = self.get_active_registrations_for_section(section,
                                                                  instructor)

        seen_registrations = {}
        for registration in registrations:
            seen_registrations[registration.person.uwregid] = True

        instructor_reg_id = instructor.uwregid if instructor else ""

        url = "/student/v4/registration.json?" + urlencode({
            "year": section.term.year,
            "quarter": section.term.quarter,
            "curriculum_abbreviation": section.curriculum_abbr,
            "course_number": section.course_number,
            "section_id": section.section_id,
            "instructor_reg_id": instructor_reg_id,
            "is_active": ""})

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        all_registration_data = []
        for reg_data in data.get("Registrations", []):
            all_registration_data.append(reg_data)

        all_registration_data.reverse()

        pws = PWS()
        for reg_data in all_registration_data:
            # Prevent duplicate registrations, the reverse() above ensures we
            # keep the latest duplicate
            if reg_data["RegID"] not in seen_registrations:
                registration = Registration()
                registration.section = section
                registration.person = pws.get_person_by_regid(reg_data["RegID"])
                registration.is_active = False
                registrations.append(registration)

                seen_registrations[reg_data["RegID"]] = True

        return registrations

    def get_active_registrations_for_section(self, section, instructor=None):
        """
        Returns a list of restclients.Registration objects, representing
        active registrations for the passed section. For independent study
        sections, the passed instructor limits registrations to that
        instructor.
        """
        instructor_reg_id = instructor.uwregid if instructor else "" 

        url = "/student/v4/registration.json?" + urlencode({
            "year": section.term.year,
            "quarter": section.term.quarter,
            "curriculum_abbreviation": section.curriculum_abbr,
            "course_number": section.course_number,
            "section_id": section.section_id,
            "instructor_reg_id": instructor_reg_id,
            "is_active": "on"})

        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        pws = PWS()
        seen_registrations = {}
        registrations = []
        for reg_data in data.get("Registrations", []):
            if reg_data["RegID"] not in seen_registrations:
                registration = Registration()
                registration.section = section
                registration.person = pws.get_person_by_regid(reg_data["RegID"])
                registration.is_active = True
                registrations.append(registration)

                seen_registrations[reg_data["RegID"]] = True

        return registrations

    def schedule_for_regid_and_term(self, regid, term):
        """
        Returns a restclients.ClassSchedule for the regid and term passed in.
        """
        dao = SWS_DAO()
        pws = PWS()
        url = "/student/v4/registration.json?" + urlencode([
            ('reg_id', regid),
            ('quarter', term.quarter),
            ('is_active', 'on'),
            ('year', term.year),
        ])

        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        term_data = json.loads(response.data)

        sections = []

        for registration in term_data["Registrations"]:
            reg_url = registration["Href"]

            # Skip a step here, and go right to the course section resource
            reg_url = re.sub('registration', 'course', reg_url)
            reg_url = re.sub('^(.*?,.*?,.*?,.*?,.*?),.*', '\\1.json', reg_url)
            reg_url = re.sub(',([^,]*).json', '/\\1.json', reg_url)
            response = dao.getURL(reg_url, {"Accept": "application/json"})

            if response.status != 200:
                raise DataFailureException(
                                            reg_url,
                                            response.status,
                                            response.data,
                                          )

            section = self._section_from_json(response.data)

            # For independent study courses, only include the one relevant 
            # instructor
            if registration["Instructor"]:
                actual_instructor = None
                regid = registration["Instructor"]["RegID"]

                for instructor in section.meetings[0].instructors:
                    if instructor.uwregid == regid:
                        actual_instructor = instructor

                if actual_instructor:
                    section.meetings[0].instructors = [ actual_instructor ]
                else:
                    section.meetings[0].instructors = [ ]
                section.independent_study_instructor_regid = registration["Instructor"]
            sections.append(section)

        schedule = ClassSchedule()
        schedule.sections = sections
        schedule.term = term

        return schedule

    def get_all_campuses(self):
        """
        Returns a list of restclients.Campus models, representing all
        campuses.
        """
        url = "/student/v4/campus.json"
        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        campuses = []
        for campus_data in data.get("Campuses", []):
            campus = Campus()
            campus.label = campus_data["CampusShortName"]
            campus.name = campus_data["CampusName"]
            campus.full_name = campus_data["CampusFullName"]
            campus.full_clean()
            campuses.append(campus)

        return campuses

    def get_all_colleges(self):
        """
        Returns a list of restclients.College models, representing all
        colleges.
        """
        url = "/student/v4/college.json"
        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        colleges = []
        for college_data in data.get("Colleges", []):
            college = College()
            college.campus_label = college_data["CampusShortName"]
            college.label = college_data["CollegeAbbreviation"]
            college.name = college_data["CollegeName"]
            college.full_name = college_data["CollegeFullName"]
            college.full_clean()
            colleges.append(college)

        return colleges

    def get_departments_for_college(self, college):
        """
        Returns a list of restclients.Department models, for the passed
        College model.
        """
        url = "/student/v4/department.json?" + urlencode({
              "college_abbreviation": college.label})
        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        departments = []
        for dept_data in data.get("Departments", []):
            department = Department()
            department.college_label = college.label
            department.label = dept_data["DepartmentAbbreviation"]
            department.name = dept_data["DepartmentFullName"]
            department.full_name = dept_data["DepartmentFullName"]
            department.full_clean()
            departments.append(department)

        return departments

    def get_curricula_for_department(self, department):
        """
        Returns a list of restclients.Curriculum models, for the passed
        Department model.
        """
        url = "/student/v4/curriculum.json?" + urlencode({
              "department_abbreviation": department.label})
        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        curricula = []
        for curr_data in data.get("Curricula", []):
            curricula.append(self._curriculum_from_json(curr_data))

        return curricula

    def get_curricula_for_term(self, term):
        """
        Returns a list of restclients.Curriculum models, for the passed
        Term model.
        """
        url = "/student/v4/curriculum.json?" + urlencode({
            "year": term.year,
            "quarter": term.quarter.lower()})
        dao = SWS_DAO()
        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)

        curricula = []
        for curr_data in data.get("Curricula", []):
            curricula.append(self._curriculum_from_json(curr_data))

        return curricula

    def _curriculum_from_json(self, data):
        """
        Returns a curriculum model created from the passed json.
        """
        curriculum = Curriculum()
        curriculum.label = data["CurriculumAbbreviation"]
        curriculum.name = data["CurriculumName"]
        curriculum.full_name = data["CurriculumFullName"]
        curriculum.full_clean()
        return curriculum

    def _term_from_json(self, data):
        """
        Returns a term model created from the passed json.
        """
        term_data = json.loads(data)

        strptime = datetime.strptime
        day_format = "%Y-%m-%d"
        datetime_format = "%Y-%m-%dT%H:%M:%S"

        term = Term()
        term.year = term_data["Year"]
        term.quarter = term_data["Quarter"]
        term.first_day_quarter = strptime(
                                    term_data["FirstDay"], day_format
                                    )

        term.last_day_instruction = strptime(
                                    term_data["LastDayOfClasses"],
                                    day_format
                                    )

        if term_data["ATermLastDay"] is not None:
            term.aterm_last_date = strptime(
                                    term_data["ATermLastDay"],
                                    day_format
                                    )

        if term_data["BTermFirstDay"] is not None:
            term.bterm_first_date = strptime(
                                    term_data["BTermFirstDay"],
                                    day_format
                                    )

        term.last_final_exam_date = strptime(
                                    term_data["LastFinalExamDay"],
                                    day_format
                                    )

        term.grading_period_open = strptime(
                                    term_data["GradingPeriodOpen"],
                                    datetime_format
                                    )

        term.grading_period_close = strptime(
                                    term_data["GradingPeriodClose"],
                                    datetime_format
                                    )

        term.grade_submission_deadline = strptime(
                                    term_data["GradeSubmissionDeadline"],
                                    datetime_format)

        term.full_clean()
        return term

    def _section_from_json(self, data):
        """
        Returns a section model created from the passed json.
        """
        pws = PWS()
        section_data = json.loads(data)

        section = Section()
        section.term = self.get_term_by_year_and_quarter(
                                section_data["Course"]["Year"],
                                section_data["Course"]["Quarter"]
                                )
        section.curriculum_abbr = section_data["Course"][
            "CurriculumAbbreviation"]
        section.course_number = section_data["Course"]["CourseNumber"]
        section.course_title = section_data["Course"]["CourseTitle"]
        section.course_title_long = section_data["Course"]["CourseTitleLong"]
        section.course_campus = section_data["CourseCampus"]
        section.section_id = section_data["SectionID"]

        section.section_type = section_data["SectionType"]
        if "independent study" == section.section_type:
            section.is_independent_study = True
        else:
            section.is_independent_study = False

        section.class_website_url = section_data["ClassWebsiteUrl"]
        section.sln = section_data["SLN"]
        if "SummerTerm" in section_data:
            section.summer_term = section_data["SummerTerm"]
        else:
            section.summer_term = ""

        section.delete_flag = section_data["DeleteFlag"]
        if "withdrawn" == section.delete_flag:
            section.is_withdrawn = True
        else:
            section.is_withdrawn = False

        primary_section = section_data["PrimarySection"]
        if (primary_section is not None and
                primary_section["SectionID"] != section.section_id):
            section.is_primary_section = False
            section.primary_section_href = primary_section["Href"]
            section.primary_section_id = primary_section["SectionID"]
            section.primary_section_curriculum_abbr = primary_section[
                "CurriculumAbbreviation"]
            section.primary_section_course_number = primary_section[
                "CourseNumber"]
        else:
            section.is_primary_section = True

        section.linked_section_urls = []
        for linked_section_type in section_data["LinkedSectionTypes"]:
            for linked_section_data in linked_section_type["LinkedSections"]:
                url = linked_section_data["Section"]["Href"]
                section.linked_section_urls.append(url)

        section.joint_section_urls = []
        for joint_section_data in section_data.get("JointSections", []):
            url = joint_section_data["Href"]
            section.joint_section_urls.append(url)

        section.meetings = []
        for meeting_data in section_data["Meetings"]:
            meeting = SectionMeeting()
            meeting.section = section
            meeting.term = section.term
            meeting.meeting_index = meeting_data["MeetingIndex"]
            meeting.meeting_type = meeting_data["MeetingType"]

            meeting.building = meeting_data["Building"]
            if meeting_data["BuildingToBeArranged"]:
                meeting.building_to_be_arranged = True
            else:
                meeting.building_to_be_arranged = False

            meeting.room_number = meeting_data["RoomNumber"]
            if meeting_data["RoomToBeArranged"]:
                meeting.room_to_be_arranged = True
            else:
                meeting.room_to_be_arranged = False

            if meeting_data["DaysOfWeekToBeArranged"]:
                meeting.days_to_be_arranged = True
            else:
                meeting.days_to_be_arranged = False

            for day_data in meeting_data["DaysOfWeek"]["Days"]:
                attribute = "meets_%s" % day_data["Name"].lower()
                setattr(meeting, attribute, True)

            meeting.start_time = meeting_data["StartTime"]
            meeting.end_time = meeting_data["EndTime"]

            meeting.instructors = []
            for instructor_data in meeting_data["Instructors"]:
                pdata = instructor_data["Person"]

                if "RegID" in pdata and pdata["RegID"] is not None:
                    instructor = pws.get_person_by_regid(pdata["RegID"])

                    if instructor is not None:
                        meeting.instructors.append(instructor)

            section.meetings.append(meeting)

        section.final_exam = None
        if "FinalExam" in section_data:
            if "MeetingStatus" in section_data["FinalExam"]:
                final_exam = FinalExam()
                final_data = section_data["FinalExam"]
                status = final_data["MeetingStatus"]
                final_exam.no_exam_or_nontraditional = False
                final_exam.is_confirmed = False
                if (status == "2") or (status == "3"):
                    final_exam.is_confirmed = True
                elif status == "1":
                    final_exam.no_exam_or_nontraditional = True

                final_exam.building = final_data["Building"]
                final_exam.room_number = final_data["RoomNumber"]

                final_format = "%Y-%m-%d : %H:%M"

                strptime = datetime.strptime
                if final_data["Date"] and final_data["Date"] != "0000-00-00":
                    if final_data["StartTime"]:
                        start_string = "%s : %s" % (
                                                    final_data["Date"],
                                                    final_data["StartTime"]
                                                    )
                        final_exam.start_date = strptime(start_string, final_format)

                    if final_data["EndTime"]:
                        end_string = "%s : %s" % (
                                                    final_data["Date"],
                                                    final_data["EndTime"]
                                                 )
                        final_exam.end_date = strptime(end_string, final_format)

                final_exam.full_clean()
                section.final_exam = final_exam

        return section
