# Generated by Django 5.1.1 on 2024-10-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myauth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars/"),
        ),
    ]
