# Generated by Django 3.2.4 on 2021-12-08 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20211112_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='date',
        ),
    ]
