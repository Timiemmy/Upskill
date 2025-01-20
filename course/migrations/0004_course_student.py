# Generated by Django 5.1.4 on 2025-01-17 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_alter_content_options_alter_module_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="student",
            field=models.ManyToManyField(
                blank=True, related_name="course_joined", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]