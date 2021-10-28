from django.utils import timezone
from django.core.management.base import BaseCommand
from notes.models import Note


class Command(BaseCommand):
    help = 'Deletes expired rows'

    def handle(self, *args, **options):
        now = timezone.now()
        Note.objects.filter(finish__lt=now).delete()
