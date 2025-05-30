from django.core.management.base import BaseCommand
from submissions.models import Submission
from journals.models import Journal
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Populate the Submission model with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        journals = list(Journal.objects.all())
        users = list(User.objects.all())

        if not journals:
            self.stdout.write(self.style.ERROR("❌ No journals found. Please seed journals first."))
            return
        if not users:
            self.stdout.write(self.style.ERROR("❌ No users found. Please create users first."))
            return

        PHASES = [choice[0] for choice in Submission.PHASE_CHOICES]
        STATUSES = [choice[0] for choice in Submission.STATUS_CHOICES]

        for _ in range(100):
            journal = random.choice(journals)
            author = random.choice(users)

            submission = Submission.objects.create(
                journal=journal,
                title=fake.sentence(nb_words=6),
                author=author,
                phase=random.choice(PHASES),
                status=random.choice(STATUSES),
                is_overdue=random.choice([True, False]),
                is_archived=random.choice([True, False]),
            )

            # Add co-authors (0–3 random ones, excluding the author)
            co_authors = random.sample(
                [user for user in users if user != author],
                k=random.randint(0, min(3, len(users) - 1))
            )
            submission.co_authors.set(co_authors)

        self.stdout.write(self.style.SUCCESS("✅ Successfully populated 100 submission records."))


# from django.core.management.base import BaseCommand
# from submissions.models import Submission
# from journals.models import Journal
# from django.contrib.auth import get_user_model
# from faker import Faker
# import random
# from datetime import timedelta, datetime

# User = get_user_model()

# # Example of allowed statuses per phase, adjust as needed:
# PHASE_STATUS_MAP = {
#     "new": ["in_progress", "author_revision", "rejected", "publication"],
#     "initial_review": ["in_progress", "author_revision", "rejected"],
#     "plagiarism": ["in_progress", "author_revision", "rejected"],
#     "desk_review": ["in_progress", "author_revision", "rejected"],
#     "peer_review": ["in_progress", "author_revision", "rejected"],
#     "decision": ["in_progress", "author_revision", "rejected"],
#     "response": ["in_progress", "author_revision"],
#     "publishing": ["publication"],
# }

# class Command(BaseCommand):
#     help = "Populate the Submission model with fake data"

#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         journals = list(Journal.objects.all())
#         users = list(User.objects.all())

#         if not journals:
#             self.stdout.write(self.style.ERROR("❌ No journals found. Please seed journals first."))
#             return
#         if not users:
#             self.stdout.write(self.style.ERROR("❌ No users found. Please create users first."))
#             return

#         for _ in range(100):
#             journal = random.choice(journals)
#             author = random.choice(users)

#             phase = random.choice(list(PHASE_STATUS_MAP.keys()))
#             possible_statuses = PHASE_STATUS_MAP[phase]
#             status = random.choice(possible_statuses)

#             # Generate submission_date within last 60 days
#             submission_date = fake.date_between(start_date='-60d', end_date='today')
#             # last_action_date should be >= submission_date
#             last_action_date = fake.date_between(start_date=submission_date, end_date='today')

#             # Determine is_overdue logically (simplified: if last_action_date is older than 10 days ago and status not final)
#             is_overdue = False
#             overdue_threshold = datetime.today().date() - timedelta(days=10)
#             if last_action_date < overdue_threshold and status not in ['rejected', 'publication']:
#                 is_overdue = True

#             submission = Submission.objects.create(
#                 journal=journal,
#                 title=fake.sentence(nb_words=6),
#                 author=author,
#                 phase=phase,
#                 status=status,
#                 submission_date=submission_date,
#                 last_action_date=last_action_date,
#                 is_overdue=is_overdue,
#                 is_archived=random.choice([True, False]),
#             )

#             # Add co-authors (0–3 random ones, excluding the author)
#             co_authors = random.sample(
#                 [user for user in users if user != author],
#                 k=random.randint(0, min(3, len(users) - 1))
#             )
#             submission.co_authors.set(co_authors)

#         self.stdout.write(self.style.SUCCESS("✅ Successfully populated 100 submission records."))
