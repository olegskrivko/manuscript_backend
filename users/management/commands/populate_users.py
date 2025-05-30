from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Populate the User model with fake users"

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.unique.clear()

        roles = ['author', 'reviewer', 'editor', 'admin']

        for _ in range(50):
            User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role=random.choice(roles),
                degree=fake.job(),
                faculty=fake.bs().title(),
                department=fake.catch_phrase(),
                university=fake.company() + " University",
                city=fake.city(),
                country=fake.country(),
                personal_webpage=fake.url(),
                is_verified=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("✅ Successfully created 50 fake users with full profile data."))
