# submissions/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Submission(models.Model):
    STATUS_CHOICES = [
        ("in_progress", "In Progress"),
        ("author_revision", "Author’s Revision"),
        ("rejected", "Rejected"),
        ("publication", "Publication Process"),
    ]

    PHASE_CHOICES = [
        ("new", "New Submission Consideration"),
        ("initial_review", "Initial Review"),
        ("plagiarism", "Plagiarism Check"),
        ("desk_review", "Desk Review"),
        ("peer_review", "Double Blind Peer Review"),
        ("decision", "Decision Making"),
        ("response", "Author’s Response"),
        ("publishing", "Publishing Process"),
    ]
    # Sortable | Visible in Listings View
    journal = models.ForeignKey("journals.Journal", on_delete=models.CASCADE)

    # Sortable | Visible in Listings View
    title = models.CharField(max_length=300)

    # Visible in Listings View | Field AUTHOR contains - (author, co_authors)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    co_authors = models.ManyToManyField(User, related_name='coauthored_submissions', blank=True)

    # Sortable | Visible in Listings View
    phase = models.CharField(max_length=30, choices=PHASE_CHOICES, default="new")
    
    # Sortable | Visible in Listings View
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="in_progress")
    
    # Sortable | Visible in Listings View
    submission_date = models.DateField(auto_now_add=True)

    # Sortable | Visible in Listings View
    last_action_date = models.DateField(auto_now=True)

    is_overdue = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)  # published or rejected

    def __str__(self):
        return f"{self.title} ({self.journal})"