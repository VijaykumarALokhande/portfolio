# Generated by Django 2.2.19 on 2021-03-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Image/')),
                ('summary', models.CharField(max_length=120)),
            ],
        ),
    ]
