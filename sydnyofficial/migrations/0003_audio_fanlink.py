# Generated by Django 3.2.18 on 2023-04-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sydnyofficial', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='fanlink',
            field=models.CharField(default='https://sydnydre.fanlink.to/hustle-up', max_length=200),
        ),
    ]