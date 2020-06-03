from rest_framework import serializers


class CustomCurrentUserDefault(serializers.CurrentUserDefault):
    def __call__(self, serializer_field):
        return super().__call__(serializer_field).profile
