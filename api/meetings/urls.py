from django.urls import path
from rest_framework.routers import DefaultRouter

from api.meetings import views

router = DefaultRouter()

router.register(r'meetings', views.MeetingViewSet, 'meetings')

urlpatterns = router.urls
