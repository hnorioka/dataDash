# Generated by Django 4.1.7 on 2023-05-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_values_datavalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
            ],
        ),
    ]
