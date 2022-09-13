"""
Configuration for the grade_event_receiver Django application.
"""


from django.apps import AppConfig


class GradeEventReceiverConfig(AppConfig):
    """
    Configuration class for the grade_event_receiver Django application.
    """
    name = 'lms.djangoapps.grade_event_receiver'
    verbose_name = "Grade Event Receiver"

    def ready(self):
        # Import the tasks module to ensure that signal handlers are registered.
        from . import signals  # pylint: disable=unused-import
