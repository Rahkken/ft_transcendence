# Generated by Django 5.1.3 on 2024-11-15 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(default='Katarina: The Sinister Blade, a deadly assassin with spinning daggers.'),
        ),
    ]
