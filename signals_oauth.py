"""
Signal handlers for the grade_event_receiver Django application.
Example of Oauth authentication.
"""
import json
from urlparse import urljoin

from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from opaque_keys.edx.keys import CourseKey, UsageKey
from requests_oauthlib import OAuth1Session

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

    url = getattr(settings, 'EXAMPLE_API_URL', {})
    path = getattr(settings, 'EXAMPLE_API_PATH', {})
    key = getattr(settings, 'EXAMPLE_API_KEY', {})
    secret = getattr(settings, 'EXAMPLE_API_SECRET', {})

    oauth_session = OAuth1Session(key, client_secret=secret)
    
    request_payload_string = json.dumps({
        'payload': {
            'course_id': course_id,
            'resource_id': problem_id,
            'user_id': user_id,
            'grade': grade,
            'max_grade': max_grade,
            'timestamp': timestamp.isoformat(),
            'submission': submission,
        },
    })
    
    endpoint = urljoin(url, path)
    try:
        response = None
        response = oauth_session.put(endpoint, request_payload_string)
        status_code = response.status_code
    except Exception as error:
            LOG.info(
                "Unable to send event to API: %s: %s: %s: %s",
                endpoint,
                request_payload_string,
                response,
                error,
            )
    