from rest_framework import serializers

from api.meetings.models import Meeting
from api.meetings import custom


class OverviewMeetingSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=custom.CustomCurrentUserDefault())

    class Meta:
        model = Meeting
        fields = ['name', 'description', 'id', 'owner']
        read_only_fields = ['id']
