# Generated by Django 3.1.4 on 2021-01-01 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20210101_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='master',
        ),
    ]
