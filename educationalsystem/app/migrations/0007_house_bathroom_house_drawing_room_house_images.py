# Generated by Django 4.2.2 on 2023-06-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_house_bathroom_remove_house_drawing_room_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='bathroom',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='drawing_room',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='images',
            field=models.ImageField(default='', max_length=50, upload_to='pics'),
        ),
    ]