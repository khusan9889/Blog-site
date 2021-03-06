# Generated by Django 4.0.5 on 2022-06-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0012_alter_post_header_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram_url',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='wevbsite_url',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
