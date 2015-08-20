"""
Interfacing with the Grad Scho Committee Request API
"""
import logging
import json
from restclients.models.grad import GradCommitteeMember, GradCommittee
from restclients.sws.person import get_person_by_regid
from restclients.grad import get_resource, datetime_from_string


PREFIX = "/services/students/v1/api/committee?id="
SUFFIX = "&status=active"


logger = logging.getLogger(__name__)


def get_committee_by_regid(regid):
    sws_person = get_person_by_regid(regid)
    if sws_person is None:
        return None
    return get_committee_by_syskey(sws_person.student_system_key)


def get_committee_by_syskey(system_key):
    if system_key is None:
        logger.info("get_committee_by_syskey abort, key is None!")
        return None
    url = "%s%s%s" % (PREFIX, system_key, SUFFIX)
    return _process_json(json.loads(get_resource(url)))


def _process_json(data):
    """
    return a list of GradCommittee objects.
    """
    requests = []
    for item in data:
        committee = GradCommittee()
        committee.status = item.get('status')
        committee.committee_type = item.get('committeeType')
        committee.dept = item.get('dept')
        committee.degree_title = item.get('degreeTitle')
        committee.degree_type = item.get('degreeType')
        committee.major_full_name = item.get('majorFullName')
        committee.start_date = datetime_from_string(item.get('startDate'))
        committee.end_date = datetime_from_string(item.get('endDate'))
        for member in item.get('members'):
            if member.get('status') == "inactive":
                continue

            com_mem = GradCommitteeMember()
            com_mem.first_name = member.get('nameFirst')
            com_mem.last_name = member.get('nameLast')
            com_mem.member_type = member.get('memberType')
            com_mem.reading_type = member.get('readingType')
            com_mem.dept = member.get('dept')
            com_mem.email = member.get('email')
            com_mem.status = member.get('status')
            committee.members.append(com_mem)

        requests.append(committee)
    return requests