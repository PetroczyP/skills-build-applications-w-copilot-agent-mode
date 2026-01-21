from django.test import TestCase
from django.urls import reverse

from .models import Team, User


class ApiRootTests(TestCase):
    def test_api_root(self):
        response = self.client.get(reverse("api-root"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)


class ModelSmokeTests(TestCase):
    def test_create_team_and_user(self):
        team = Team.objects.create(name="Team Marvel")
        user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=team.name)
        self.assertEqual(user.team, team.name)
