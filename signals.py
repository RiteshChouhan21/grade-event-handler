"""
Signal handlers for the grade_event_receiver Django application.
"""

from django.contrib.auth.models import User
from django.dispatch import receiver
from opaque_keys.edx.keys import CourseKey, UsageKey

from lms.djangoapps.grades.api import signals as grades_signals


@receiver(grades_signals.PROBLEM_RAW_SCORE_CHANGED)
def custom_problem_raw_score_changed_handler(sender, **kwargs):  # pylint: disable=unused-argument
    """
    Handles the raw score changed signal, converting the score to a
    weighted score and firing the PROBLEM_RAW_SCORE_CHANGED signal.
    """
    user_id = kwargs['user_id']
    course_id = kwargs['course_id']
    usage_id = kwargs['usage_id']
    score_earned = kwargs['raw_earned']

    # user = User.objects.get(id=user_id)
    # course_key = CourseKey.from_string(course_id)
    # usage_key = UsageKey.from_string(usage_id).map_into_course(course_key)

    # import pdb;pdb.set_trace()
