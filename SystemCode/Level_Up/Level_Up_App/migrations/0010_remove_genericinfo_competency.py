# Generated by Django 2.2.3 on 2019-08-18 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Level_Up_App', '0009_genericinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genericinfo',
            name='competency',
        ),
    ]