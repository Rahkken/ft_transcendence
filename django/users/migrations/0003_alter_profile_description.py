# Generated by Django 5.1.3 on 2024-11-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_friends_profile_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(default='Yasuo: The Unforgiven, a swordsman with wind-based abilities and a powerful ultimate.'),
        ),
    ]
