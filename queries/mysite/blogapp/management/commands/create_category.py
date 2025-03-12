from django.core.management import BaseCommand

from blogapp.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = [
            'Scary',
            'Detective',
            'No category',
            'Special News',
            'All',
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {category}'))
