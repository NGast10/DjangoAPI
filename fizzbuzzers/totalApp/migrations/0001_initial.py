# Generated by Django 5.0.3 on 2024-03-24 03:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="fizzBuzz",
            fields=[
                (
                    "id",
                    models.CharField(max_length=1, primary_key=True, serialize=False),
                ),
                ("userAgent", models.CharField(max_length=165)),
                (
                    "creationDate",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("message", models.CharField(max_length=50)),
            ],
        ),
    ]
