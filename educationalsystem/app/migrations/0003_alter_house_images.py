# Generated by Django 4.2.2 on 2023-06-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_house_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='images',
            field=models.ImageField(default='', max_length=50, upload_to='pics'),
        ),
    ]
