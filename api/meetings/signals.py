from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from api.meetings.models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    Profile.objects.create(user=instance)
