# Generated by Django 2.2.6 on 2021-01-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('arrival_date', models.DateField(auto_now_add=True)),
                ('breed', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
