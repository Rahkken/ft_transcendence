# Generated by Django 5.1.3 on 2024-11-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_room_name_alter_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(db_default="'room_' + user1_id +''+user2_id", max_length=200),
        ),
    ]
