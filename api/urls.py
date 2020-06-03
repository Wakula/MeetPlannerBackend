from django.urls import path, include
from django.http import HttpResponse
import json
import datetime


class MeetPlannerJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def foo(request):
    data = {
        'data': datetime.datetime.now()
    }
    data = MeetPlannerJSONEncoder().encode(data)

    return HttpResponse(data)


urlpatterns = [
    path('api/', include('api.meetings.urls')),
    path('api/', include('api.accounts.urls')),
]
