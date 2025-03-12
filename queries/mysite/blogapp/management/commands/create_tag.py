from django.core.management import BaseCommand
from blogapp.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        tags = [
            'News',
            'About of all',
            'Something scary',
            'Any',
        ]

        for tag_name in tags:
            Tag.objects.get_or_create(name=tag_name)
        self.stdout.write(self.style.SUCCESS('Successfully created tags'))