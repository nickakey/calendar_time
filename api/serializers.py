from rest_framework import serializers
from .models import EventModel


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventModel
        fields = ("title", "count", "total_minutes",
                  "category", "id")
