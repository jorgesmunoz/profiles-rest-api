# Generated by Django 3.2.12 on 2022-04-03 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20220403_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_staff',
        ),
    ]