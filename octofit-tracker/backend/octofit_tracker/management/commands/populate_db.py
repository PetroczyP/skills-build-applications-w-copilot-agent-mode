from django.core.management.base import BaseCommand
from django.utils import timezone

from octofit_tracker.models import Activity, LeaderboardEntry, Team, User, Workout


class Command(BaseCommand):
    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **options):
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        teams = Team.objects.bulk_create(
            [
                Team(
                    name="Team Marvel",
                    description="Heroes united to push their limits.",
                    motto="Stronger together.",
                ),
                Team(
                    name="Team DC",
                    description="Legends training for the next big challenge.",
                    motto="Justice through fitness.",
                ),
            ]
        )

        users = User.objects.bulk_create(
            [
                User(
                    name="Iron Man",
                    email="ironman@marvel.com",
                    team=teams[0].name,
                    age=35,
                ),
                User(
                    name="Captain Marvel",
                    email="captainmarvel@marvel.com",
                    team=teams[0].name,
                    age=32,
                ),
                User(
                    name="Black Panther",
                    email="blackpanther@marvel.com",
                    team=teams[0].name,
                    age=30,
                ),
                User(
                    name="Batman",
                    email="batman@dc.com",
                    team=teams[1].name,
                    age=36,
                ),
                User(
                    name="Wonder Woman",
                    email="wonderwoman@dc.com",
                    team=teams[1].name,
                    age=3000,
                ),
                User(
                    name="The Flash",
                    email="flash@dc.com",
                    team=teams[1].name,
                    age=28,
                ),
            ]
        )

        Activity.objects.bulk_create(
            [
                Activity(
                    user_email=users[0].email,
                    activity_type="Arc Reactor HIIT",
                    duration_minutes=45,
                    calories=420,
                ),
                Activity(
                    user_email=users[1].email,
                    activity_type="Cosmic Endurance Run",
                    duration_minutes=60,
                    calories=560,
                ),
                Activity(
                    user_email=users[2].email,
                    activity_type="Wakanda Strength Training",
                    duration_minutes=50,
                    calories=480,
                ),
                Activity(
                    user_email=users[3].email,
                    activity_type="Gotham Rooftop Sprints",
                    duration_minutes=40,
                    calories=400,
                ),
                Activity(
                    user_email=users[4].email,
                    activity_type="Amazon Circuit",
                    duration_minutes=55,
                    calories=520,
                ),
                Activity(
                    user_email=users[5].email,
                    activity_type="Speed Force Intervals",
                    duration_minutes=35,
                    calories=380,
                ),
            ]
        )

        LeaderboardEntry.objects.bulk_create(
            [
                LeaderboardEntry(team=teams[0].name, points=1560, rank=1),
                LeaderboardEntry(team=teams[1].name, points=1490, rank=2),
            ]
        )

        Workout.objects.bulk_create(
            [
                Workout(
                    title="Infinity Circuit",
                    description="Full-body power circuit inspired by the Avengers.",
                    difficulty="Advanced",
                    duration_minutes=50,
                    target_muscle="Full Body",
                ),
                Workout(
                    title="Gotham Strength",
                    description="Explosive strength routine for vigilant heroes.",
                    difficulty="Intermediate",
                    duration_minutes=45,
                    target_muscle="Upper Body",
                ),
                Workout(
                    title="Speed Force Cardio",
                    description="High-intensity cardio to build lightning speed.",
                    difficulty="Beginner",
                    duration_minutes=30,
                    target_muscle="Cardio",
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("octofit_db populated with test data."))
