# Generated by Django 3.2.12 on 2022-04-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_remove_userprofile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
