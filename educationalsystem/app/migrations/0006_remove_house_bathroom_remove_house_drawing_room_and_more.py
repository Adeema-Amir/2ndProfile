# Generated by Django 4.2.2 on 2023-06-20 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_myself'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='house',
            name='drawing_room',
        ),
        migrations.RemoveField(
            model_name='house',
            name='images',
        ),
    ]