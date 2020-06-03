from rest_framework.viewsets import ModelViewSet
from api.meetings import models
from api.meetings import serializers


class MeetingViewSet(ModelViewSet):
    queryset = models.Meeting.objects.get_overview_data()
    serializer_class = serializers.OverviewMeetingSerializer
