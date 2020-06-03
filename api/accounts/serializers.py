from rest_framework import serializers
from api.accounts.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        password = self.validated_data['password']

        user = User(
            email=self.validated_data['email']
        )

        user.set_password(password)
        user.save()
        return user
