# Generated by Django 4.0.3 on 2022-03-21 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0008_profile_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tech_stack',
        ),
    ]
