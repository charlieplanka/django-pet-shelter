# Generated by Django 2.2.6 on 2021-01-14 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shelter', '0008_auto_20210114_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='species',
        ),
    ]