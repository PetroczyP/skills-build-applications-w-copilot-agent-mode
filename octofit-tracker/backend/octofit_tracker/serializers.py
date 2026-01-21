from bson import ObjectId
from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, User, Workout


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
        if "id" in data and data["id"] is not None:
            data["id"] = str(data["id"])
        return data


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TeamSerializer(BaseSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class ActivitySerializer(BaseSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class LeaderboardEntrySerializer(BaseSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = "__all__"


class WorkoutSerializer(BaseSerializer):
    class Meta:
        model = Workout
        fields = "__all__"
