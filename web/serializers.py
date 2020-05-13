from rest_framework import serializers

from web.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
        )
        read_only_fields = (
            'id', 'first_name',
        )
