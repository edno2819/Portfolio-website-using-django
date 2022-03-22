# Generated by Django 4.0.3 on 2022-03-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_project_profile_pic_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fb_link',
            new_name='medium_link',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='github_link',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='blog',
            name='link',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='experience',
            name='responsibilities_1',
            field=models.CharField(blank=True, default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='experience',
            name='responsibilities_2',
            field=models.CharField(blank=True, default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='experience',
            name='responsibilities_3',
            field=models.CharField(blank=True, default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='experience',
            name='responsibilities_4',
            field=models.CharField(blank=True, default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='summary',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
