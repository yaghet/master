from django.core.management import BaseCommand
from blogapp.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creating author")
        authors_data = [
            {
                "name": "Creator",
                "bio": "No Bio yet",
            },
            {
                "name": "Daniel",
                "bio": "I'm a new author!",
            },
        ]
        for author_data in authors_data:
            Author.objects.get_or_create(
                name=author_data["name"],
                bio=author_data["bio"])
        self.stdout.write(self.style.SUCCESS("Successfully created authors"))
