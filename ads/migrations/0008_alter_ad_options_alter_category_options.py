# Generated by Django 4.1.3 on 2022-11-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_category_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
