# Generated by Django 2.2.19 on 2021-03-09 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempo',
            name='topic',
        ),
    ]
