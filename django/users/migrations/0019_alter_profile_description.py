# Generated by Django 5.1.3 on 2024-11-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(default='Zed: The Master of Shadows, a ninja assassin with shadow clones.'),
        ),
    ]
