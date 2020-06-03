from django.apps import AppConfig


class MeetingsConfig(AppConfig):
    name = 'api.meetings'

    def ready(self):
        import api.meetings.signals
