# Generated by Django 5.1.1 on 2024-09-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0003_education_gpa_profile_career_objective_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
