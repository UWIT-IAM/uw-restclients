from django.conf import settings
from restclients.canvas import Canvas
from restclients.dao import Canvas_DAO
from restclients.exceptions import DataFailureException
from restclients.models.canvas import Report, ReportType
import json


class Reports(Canvas):
    def get_available_reports(self):
        """
        Returns the list of reports for the current context.
        
        https://canvas.instructure.com/doc/api/account_reports.html#method.account_reports.available_reports
        """
        data = self._get_resource("/api/v1/accounts/%s/reports.json" % (
                                  settings.RESTCLIENTS_CANVAS_ACCOUNT_ID))

        report_types = []
        for datum in data:
            report_type = ReportType()
            report_type.name = datum["report"]
            report_type.title = datum["title"]
            report_type.parameters = datum["parameters"]
            if datum["last_run"] is not None:
                report = self._report_from_json(datum["last_run"])
                report_type.last_run = report

            report_types.append(report_type)

        return report_types

    def get_reports_by_type(self, report_type):
        """
        Shows all reports of the passed report_type that have been run
        for the account.

        https://canvas.instructure.com/doc/api/account_reports.html#method.account_reports.index
        """
        data = self._get_resource("/api/v1/accounts/%s/reports/%s.json" % (
                                  settings.RESTCLIENTS_CANVAS_ACCOUNT_ID,
                                  report_type))

        reports = []
        for datum in data:
            reports.append(self._report_from_json(datum))

        return reports

    def create_report(self, report_type, parameters={}):
        """
        Generates a report instance for the account.

        https://canvas.instructure.com/doc/api/account_reports.html#method.account_reports.create
        """
        dao = Canvas_DAO()

        url = "/api/v1/accounts/%s/reports/%s.json" % (
            settings.RESTCLIENTS_CANVAS_ACCOUNT_ID, report_type)
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json"}
        body = json.dumps(parameters)

        response = dao.postURL(url, headers, body)

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        report_data = json.loads(response.data)

        return self._report_from_json(report_data)

    def get_report_status(self, report):
        """
        Returns the status of a report.

        https://canvas.instructure.com/doc/api/account_reports.html#method.account_reports.show
        """
        dao = Canvas_DAO()

        url = "/api/v1/accounts/%s/reports/%s/%s.json" % (
            settings.RESTCLIENTS_CANVAS_ACCOUNT_ID, report.type,
            report.report_id)

        response = dao.getURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        report_data = json.loads(response.data)

        return self._report_from_json(report_data)

    def delete_report(self, report):
        """
        Deletes a generated report instance.

        https://canvas.instructure.com/doc/api/account_reports.html#method.account_reports.destroy
        """
        dao = Canvas_DAO()

        url = "/api/v1/accounts/%s/reports/%s/%s.json" % (
            settings.RESTCLIENTS_CANVAS_ACCOUNT_ID, report.type,
            report.report_id)

        response = dao.deleteURL(url, {"Accept": "application/json"})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        report_data = json.loads(response.data)

        return self._report_from_json(report_data)

    def _report_from_json(self, data):
        report = Report()
        report.report_id = data["id"]
        report.type = data["report"]
        report.url = data["file_url"]
        report.status = data["status"]
        report.progress = data["progress"]
        report.parameters = data["parameters"]

        return report
