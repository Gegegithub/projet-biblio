# Generated by Django 4.2.16 on 2024-11-07 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('auth_app', '0002_customuser_delete_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='utilisateur',
        ),
    ]
