from django.core.management.base import BaseCommand
from submissions.tasks import mark_overdue_submissions

class Command(BaseCommand):
    help = 'Marks overdue submissions based on phase durations.'

    def handle(self, *args, **options):
        mark_overdue_submissions()
        self.stdout.write(self.style.SUCCESS("Overdue submissions marked successfully."))
