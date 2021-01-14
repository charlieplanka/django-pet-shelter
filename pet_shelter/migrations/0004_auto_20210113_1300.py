# Generated by Django 2.2.6 on 2021-01-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shelter', '0003_auto_20210111_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, upload_to='pet_photos'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.CharField(choices=[('Ж', 'Ж'), ('М', 'М'), ('Неизвестно', 'Неизвестно')], default='Неизвестно', max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(blank=True, choices=[('Собаки', 'Собаки'), ('Коты и кошки', 'Коты и кошки'), ('Кролики', 'Кролики')], max_length=100),
        ),
    ]