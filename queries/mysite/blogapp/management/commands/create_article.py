import random
from django.core.management import BaseCommand
from blogapp.models import Article, Author, Tag, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles_data = [
            {'title': 'Some', 'content': 'No content',},
            {'title': 'Another', 'content': 'Two article on my site',},
            {'title': 'Just Title', 'content': 'Added for read',},
            {'title': 'New title', 'content': 'No comments',},
        ]
        authors = list(Author.objects.values_list('id', flat=True))
        categories = list(Category.objects.values_list('id', flat=True))
        tags = list(Tag.objects.values_list('id', flat=True))

        for article_data in articles_data:
            article = Article(
                title=article_data.get('title'),
                content=article_data.get('content'),
                author_id=random.choice(authors),
                category_id=random.choice(categories),
            )
            article.save()
            article.tags.set(random.sample(tags, random.randint(1, min(3, len(tags)))))

        self.stdout.write(self.style.SUCCESS('Successfully created all articles'))