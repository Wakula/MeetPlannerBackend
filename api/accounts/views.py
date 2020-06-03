from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.accounts import serializers


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]

    serializer_class = serializers.RegistrationSerializer
