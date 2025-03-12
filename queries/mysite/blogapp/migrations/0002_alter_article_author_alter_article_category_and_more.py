# Generated by Django 5.1.1 on 2025-03-12 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="blogapp.author",
                verbose_name="Author",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="blogapp.category",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(verbose_name="Article Content"),
        ),
        migrations.AlterField(
            model_name="article",
            name="pub_date",
            field=models.DateTimeField(verbose_name="Publication Date"),
        ),
        migrations.AlterField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(to="blogapp.tag", verbose_name="Tags"),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Article Title"),
        ),
        migrations.AlterField(
            model_name="author",
            name="bio",
            field=models.TextField(
                blank=True,
                help_text="Optional biography of the author.",
                null=True,
                verbose_name="Biography",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=40, verbose_name="Category Name"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=20, verbose_name="Tag Name"),
        ),
    ]
