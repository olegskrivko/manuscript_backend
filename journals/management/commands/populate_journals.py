from django.core.management.base import BaseCommand
from journals.models import Journal
from faker import Faker
import random

class Command(BaseCommand):
    help = "Populate the Journal model with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        statuses = ["Active", "Inactive"]

        for _ in range(100):
            Journal.objects.create(
                journal_title=fake.sentence(nb_words=4),
                issn_print=fake.isbn13(),
                issn_online=fake.isbn13(),
                status=random.choice(statuses),
                publisher=fake.company(),
                founder=fake.name(),
                issued_since_month=random.choice(months),
                issued_since_year=random.randint(1980, 2025)
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully populated 100 journal records.'))

# python manage.py populate_journals