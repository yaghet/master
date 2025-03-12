from django.db import models


class Author(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100)
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='Biography',
        help_text='Optional biography of the author.'
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=40, verbose_name='Category Name')

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=20, verbose_name='Tag Name')

    def __str__(self):
        return self.name


class Article(models.Model):

    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=200, verbose_name='Article Title')
    content = models.TextField(verbose_name='Article Content')
    pub_date = models.DateTimeField(verbose_name='Publication Date', auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    tags = models.ManyToManyField(Tag, verbose_name='Tags')

    def __str__(self):
        return self.title
