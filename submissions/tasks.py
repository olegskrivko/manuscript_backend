
from datetime import timedelta
from django.utils.timezone import now
from .models import Submission
from workalendar.europe import Latvia

# Latvian working calendar
cal = Latvia()

# Phase + Status duration matrix (in working days)
# This defines how long a submission can stay in a specific phase/status before becoming overdue.
PHASE_STATUS_DUE_DAYS = {
    ("new", "in_progress"): 1,
    ("initial_review", "in_progress"): 1,
    ("plagiarism", "in_progress"): 1,
    ("desk_review", "in_progress"): 3,
    ("peer_review", "in_progress"): 1,
    ("peer_review", "author_revision"): 4,
    ("decision", "in_progress"): 2,
    ("response", "in_progress"): 2,
    ("publishing", "publication"): None,  # Final stage, no time limit
    # Add more if needed
}

def add_working_days(start_date, working_days):
    """
    Calculate the date after adding a number of Latvian working days to a given start date.

    Args:
        start_date (date): The date from which to start counting.
        working_days (int): The number of working days to add.

    Returns:
        date: The resulting date after skipping non-working days (weekends + Latvian holidays).
    """
    current_date = start_date
    added = 0
    while added < working_days:
        current_date += timedelta(days=1)
        if cal.is_working_day(current_date):
            added += 1
    return current_date

def mark_overdue_submissions():
    """
    Check all non-archived submissions and mark them as overdue if they exceed the allowed
    number of working days in their current phase and status.

    This function compares the last_action_date against today's date using Latvian working days,
    and updates the `is_overdue` field accordingly.
    """
    today = now().date()
    submissions = Submission.objects.filter(is_archived=False)

    for submission in submissions:
        key = (submission.phase, submission.status)
        allowed_days = PHASE_STATUS_DUE_DAYS.get(key)

        # Skip if no duration is defined or the status is 'rejected'
        if allowed_days is None or submission.status == "rejected":
            continue 

        deadline = add_working_days(submission.last_action_date, allowed_days)
        is_late = today > deadline

        if submission.is_overdue != is_late:
            submission.is_overdue = is_late
            submission.save(update_fields=["is_overdue"])
