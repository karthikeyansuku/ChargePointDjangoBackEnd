# Generated by Django 3.1.7 on 2021-09-13 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataModel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='slots_available',
        ),
    ]
