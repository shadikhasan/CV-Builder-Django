# Generated by Django 5.1.1 on 2024-09-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='proficiency',
            field=models.PositiveIntegerField(default=80),
        ),
    ]
