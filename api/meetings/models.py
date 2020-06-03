from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from api.meetings.managers import MeetingManager


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def is_owner(self, meeting):
        return self == meeting.owner


class Meeting(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='meetings')
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    objects = MeetingManager()

    def __str__(self):
        return self.title
