# Generated by Django 3.2.4 on 2021-11-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_data_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='user_id',
            field=models.TextField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='data',
            name='data',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
