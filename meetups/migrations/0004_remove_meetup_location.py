# Generated by Django 3.2.8 on 2021-11-14 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_auto_20211114_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
    ]
