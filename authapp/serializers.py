from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    is_superuser = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_superuser']

    def get_is_superuser(self, obj):
        return obj.is_staff