# Generated by Django 4.1.3 on 2022-11-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_alter_location_lat_alter_location_lng'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Локация', 'verbose_name_plural': 'Локации'},
        ),
    ]
