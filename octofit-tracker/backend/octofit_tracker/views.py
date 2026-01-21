from rest_framework import routers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Activity, LeaderboardEntry, Team, User, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"teams", TeamViewSet)
router.register(r"activities", ActivityViewSet)
router.register(r"leaderboard", LeaderboardEntryViewSet)
router.register(r"workouts", WorkoutViewSet)


@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "users": request.build_absolute_uri("/api/users/"),
            "teams": request.build_absolute_uri("/api/teams/"),
            "activities": request.build_absolute_uri("/api/activities/"),
            "leaderboard": request.build_absolute_uri("/api/leaderboard/"),
            "workouts": request.build_absolute_uri("/api/workouts/"),
        }
    )
