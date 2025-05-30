from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

# class Command(BaseCommand):
#     help = "Delete all non-superuser users"

#     def handle(self, *args, **kwargs):
#         deleted_count, _ = User.objects.filter(is_superuser=False).delete()
#         self.stdout.write(self.style.WARNING(f"⚠️ Deleted {deleted_count} user(s) (excluding superusers)."))

class Command(BaseCommand):
    help = "Delete ALL users including superusers (use with caution!)"

    def handle(self, *args, **kwargs):
        confirm = input("Are you sure you want to delete ALL users? Type 'yes' to confirm: ")
        if confirm == 'yes':
            deleted_count, _ = User.objects.all().delete()
            self.stdout.write(self.style.ERROR(f"🗑️ Deleted {deleted_count} user(s) including superusers."))
        else:
            self.stdout.write("❌ Operation cancelled.")

