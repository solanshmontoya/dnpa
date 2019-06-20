from datetime import datetime, timedelta, date


from .models import Notification, Store
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('name', 'image', 'description',)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('latitude', 'length', 'address',)

class NotificationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields = ('id',) 