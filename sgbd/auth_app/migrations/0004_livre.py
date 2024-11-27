# Generated by Django 4.2.16 on 2024-11-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_rename_customuser_utilisateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('auteur', models.CharField(blank=True, max_length=100)),
                ('resume', models.TextField()),
                ('nombre_exemplaires', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
