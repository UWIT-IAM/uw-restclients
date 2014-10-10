from restclients.sws.v4.section import get_sections_by_instructor_and_term as v4_get_sections_by_instructor_and_term
from restclients.sws.v4.section import get_sections_by_delegate_and_term as v4_get_sections_by_delegate_and_term
from restclients.sws.v4.section import get_sections_by_curriculum_and_term as v4_get_sections_by_curriculum_and_term
from restclients.sws.v4.section import get_section_by_url as v4_get_section_by_url
from restclients.sws.v4.section import get_section_by_label as v4_get_section_by_label
from restclients.sws.v4.section import get_linked_sections as v4_get_linked_sections
from restclients.sws.v4.section import get_joint_sections as v4_get_joint_sections
from restclients.sws.v5.section import get_sections_by_instructor_and_term as v5_get_sections_by_instructor_and_term
from restclients.sws.v5.section import get_sections_by_delegate_and_term as v5_get_sections_by_delegate_and_term
from restclients.sws.v5.section import get_sections_by_curriculum_and_term as v5_get_sections_by_curriculum_and_term
from restclients.sws.v5.section import get_section_by_url as v5_get_section_by_url
from restclients.sws.v5.section import get_section_by_label as v5_get_section_by_label
from restclients.sws.v5.section import get_linked_sections as v5_get_linked_sections
from restclients.sws.v5.section import get_joint_sections as v5_get_joint_sections
from restclients.sws import use_v5_resources

def get_sections_by_instructor_and_term(*args, **kwargs):
    if use_v5_resources():
        return v5_get_sections_by_instructor_and_term(*args, **kwargs)
    else:
        return v4_get_sections_by_instructor_and_term(*args, **kwargs)

def get_sections_by_delegate_and_term(*args, **kwargs):
    if use_v5_resources():
        return v5_get_sections_by_delegate_and_term(*args, **kwargs)
    else:
        return v4_get_sections_by_delegate_and_term(*args, **kwargs)

def get_sections_by_curriculum_and_term(*args, **kwargs):
    if use_v5_resources():
        return v5_get_sections_by_curriculum_and_term(*args, **kwargs)
    else:
        return v4_get_sections_by_curriculum_and_term(*args, **kwargs)

def get_section_by_url(*args, **kwargs):
    if use_v5_resources():
        return v5_get_section_by_url(*args, **kwargs)
    else:
        return v4_get_section_by_url(*args, **kwargs)

def get_section_by_label(*args, **kwargs):
    if use_v5_resources():
        return v5_get_section_by_label(*args, **kwargs)
    else:
        return v4_get_section_by_label(*args, **kwargs)

def get_linked_sections(*args, **kwargs):
    if use_v5_resources():
        return v5_get_linked_sections(*args, **kwargs)
    else:
        return v4_get_linked_sections(*args, **kwargs)

def get_joint_sections(*args, **kwargs):
    if use_v5_resources():
        return v5_get_joint_sections(*args, **kwargs)
    else:
        return v4_get_joint_sections(*args, **kwargs)

