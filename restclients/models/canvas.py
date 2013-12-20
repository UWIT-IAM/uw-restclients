from django.db import models


class Account(models.Model):
    account_id = models.IntegerField(max_length=20)
    sis_account_id = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=500)
    parent_account_id = models.CharField(max_length=30)
    root_account_id = models.CharField(max_length=30)

    class Meta:
        db_table = "restclients_canvas_account"


class Term(models.Model):
    term_id = models.IntegerField(max_length=20)
    sis_term_id = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_canvas_term"


class Course(models.Model):
    course_id = models.IntegerField(max_length=20)
    sis_course_id = models.CharField(max_length=100, null=True)
    account_id = models.IntegerField(max_length=20)
    term = models.ForeignKey(Term, null=True)
    course_name = models.CharField(max_length=200)
    course_url = models.CharField(max_length=2000)

    def sws_course_id(self):
        if self.sis_course_id is None:
            return None

        parts = self.sis_course_id.split("-")
        if len(parts) != 5:
            return None

        sws_id = "%s,%s,%s,%s/%s" % (parts[0], parts[1], parts[2], parts[3],
                                     parts[4])

        return sws_id

    class Meta:
        db_table = "restclients_canvas_course"


class Section(models.Model):
    section_id = models.IntegerField(max_length=20)
    sis_section_id = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=200)
    course_id = models.IntegerField(max_length=20)
    nonxlist_course_id = models.IntegerField(max_length=20)

    class Meta:
        db_table = "restclients_canvas_section"


class Enrollment(models.Model):
    STUDENT = "StudentEnrollment"
    TEACHER = "TeacherEnrollment"
    TA = "TaEnrollment"
    OBSERVER = "ObserverEnrollment"
    DESIGNER = "DesignerEnrollment"

    ROLE_CHOICES = (
        (STUDENT, "Student"),
        (TEACHER, "Teacher"),
        (TA, "TA"),
        (OBSERVER, "Observer"),
        (DESIGNER, "Designer")
    )

    user_id = models.IntegerField(max_length=20)
    course_id = models.IntegerField(max_length=20)
    section_id = models.IntegerField(max_length=20)
    login_id = models.CharField(max_length=80)
    role = models.CharField(max_length=80, choices=ROLE_CHOICES)
    status = models.CharField(max_length=100)
    html_url = models.CharField(max_length=1000)
    sis_course_id = models.CharField(max_length=100, null=True)
    course_url = models.CharField(max_length=2000, null=True)
    course_name = models.CharField(max_length=100, null=True)
    current_score = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    final_score = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    current_grade = models.TextField(max_length=12, null=True)
    final_grade = models.TextField(max_length=12, null=True)
    grade_html_url = models.CharField(max_length=1000)

    def sws_course_id(self):
        if self.sis_course_id is None:
            return None

        parts = self.sis_course_id.split("-")

        if len(parts) != 5:
            return None

        sws_id = "%s,%s,%s,%s/%s" % (parts[0], parts[1], parts[2], parts[3],
                                     parts[4])

        return sws_id

    class Meta:
        db_table = "restclients_canvas_enrollment"


class Attachment(models.Model):
    attachment_id = models.IntegerField(max_length=20)
    filename = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200)
    content_type = models.CharField(max_length=50)
    size = models.IntegerField(max_length=20)
    url = models.CharField(max_length=500)

    class Meta:
        db_table = "restclients_canvas_attachment"


class Report(models.Model):
    report_id = models.IntegerField(max_length=20)
    account_id = models.IntegerField(max_length=20)
    type = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    progress = models.SmallIntegerField(max_length=3, default=0)
    attachment = models.ForeignKey(Attachment, null=True)

    class Meta:
        db_table = "restclients_canvas_report"


class ReportType(models.Model):
    PROVISIONING = "provisioning_csv"
    SIS_EXPORT = "sis_export_csv"
    UNUSED_COURSES = "unused_courses_csv"

    NAME_CHOICES = (
        (PROVISIONING, "Provisioning"),
        (SIS_EXPORT, "SIS Export"),
        (UNUSED_COURSES, "Unused Courses")
    )

    name = models.CharField(max_length=500, choices=NAME_CHOICES)
    title = models.CharField(max_length=500)

    class Meta:
        db_table = "restclients_canvas_reporttype"


class User(models.Model):
    user_id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=100, null=True)
    short_name = models.CharField(max_length=100, null=True)
    sortable_name = models.CharField(max_length=100, null=True)
    sis_user_id = models.CharField(max_length=100, null=True)
    login_id = models.CharField(max_length=100, null=True)
    time_zone = models.CharField(max_length=100, null=True)
    locale = models.CharField(max_length=2, null=True)
    email = models.CharField(max_length=100, null=True)

    def post_data(self):
        return {"user": {"name": self.name,
                         "short_name": self.short_name,
                         "sortable_name": self.sortable_name,
                         "time_zone": self.time_zone,
                         "locale": self.locale},
                "pseudonym": {"unique_id": self.login_id,
                              "sis_user_id": self.sis_user_id,
                              "send_confirmation": False}}

    class Meta:
        db_table = "restclients_canvas_user"


class Admin(models.Model):
    admin_id = models.IntegerField(max_length=20)
    role = models.CharField(max_length=100)
    user = models.ForeignKey(User)

    class Meta:
        db_table = "restclients_canvas_admin"


class Submission(models.Model):
    submission_id = models.IntegerField(max_length=20)
    body = models.TextField(null=True)
    attempt = models.IntegerField(max_length=2)
    submitted_at = models.DateTimeField()
    assignment_id = models.IntegerField(max_length=20)
    workflow_state = models.CharField(max_length=100, null=True)
    preview_url = models.CharField(max_length=500)
    late = models.BooleanField()
    grade = models.TextField(max_length=12, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    grade_matches_current_submission = models.BooleanField()
    url = models.CharField(max_length=500, null=True)
    grader_id = models.IntegerField(max_length=20)
    graded_at = models.DateTimeField(null=True)
    submission_type = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_canvas_submission"


class Assignment(models.Model):
    assignment_id = models.IntegerField(max_length=20)
    due_at = models.DateTimeField(null=True)
    points_possible = models.IntegerField(max_length=8)
    position = models.IntegerField(max_length=8)
    name = models.CharField(max_length=500)
    muted = models.BooleanField()
    html_url = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = "restclients_canvas_assignment"


class Quiz(models.Model):
    quiz_id = models.IntegerField(max_length=20)
    due_at = models.DateTimeField()
    title = models.CharField(max_length=500)
    html_url = models.CharField(max_length=500, null=True)
    published = models.BooleanField()

    class Meta:
        db_table ="restclients_canvas_quiz" 

